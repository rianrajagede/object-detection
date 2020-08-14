from PIL import Image
import numpy as np
import os
import xml.etree.ElementTree as ET
import tqdm

max_dim = 250
path = "test_resize/"

# RESIZE THE IMAGE

for f in tqdm.tqdm(os.listdir(path)):
    if f.split(".")[-1].lower() in ["jpg", "jpeg", "png"]:
        
        file_name = f
        name = file_name.split(".")[0]

        img = Image.open(path + file_name)
        img_size = np.array(img).shape

        height = img_size[0]
        width = img_size[1]
        ratio = 0
        if height > width:
            new_h = max_dim
            ratio = new_h / height
            new_w = int(width * ratio)
        else:
            new_w = max_dim
            ratio = new_w / width
            new_h = int(height * ratio)

        new_img = img.resize((new_w, new_h))
        new_img.save(path + file_name, "JPEG", optimize=True)

        # RESIZE THE XML

        tree = ET.parse(path + name + ".xml")
        root = tree.getroot()

        for box in root.findall('object/bndbox'):
            box.find("xmin").text = str(int(int(box.find("xmin").text)*ratio))
            box.find("xmax").text = str(int(int(box.find("xmax").text)*ratio))
            box.find("ymin").text = str(int(int(box.find("ymin").text)*ratio))
            box.find("ymax").text = str(int(int(box.find("ymax").text)*ratio))

        tree.write(path + name + ".xml")