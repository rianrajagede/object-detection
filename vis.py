# CHECK

from PIL import Image
from PIL import ImageDraw
import xml.etree.ElementTree as ET

filename = "test_resize/00001.jpg"
name = filename.split(".")[0]
image = Image.open(filename)

tree = ET.parse(name + ".xml")
root = tree.getroot()

for box in root.findall('object/bndbox'):
    xmin = int(box.find("xmin").text)
    ymin = int(box.find("ymin").text)
    xmax = int(box.find("xmax").text)
    ymax = int(box.find("ymax").text)
    draw = ImageDraw.Draw(image)
    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline ="red")
image.show()