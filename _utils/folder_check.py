"""
run:
python folder_check.py --rootdir "Prioritas 1"

untuk memastikan apakah pada semua folder, jumlah image dan xml nya sama
kalau ada yang tidak sama, akan dioutputkan

identified bug:
kadang perlu dirun beberapa kali
"""
import os
import argparse
import xml.etree.ElementTree as ET
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--rootdir', help='rootdir contains subdir of images and annots',
                    required=True)
args = parser.parse_args()
image_types = ["png", "PNG", "jpg", "jpeg", "JPG", "JPEG"]

root_dir = args.rootdir

all_files_xml = []
all_files_img = []
all_path = [] # for debugging
for root, subdirs, files in os.walk(root_dir):
    x = []
    y = []
    for f in files:
        if len(files)>0:
            if f.split(".")[-1] in image_types:
                x.append([f, root])
            if f.split(".")[-1] in ["xml"]:
                y.append([f, root])
    if(len(x)!=len(y)):
        print(root)