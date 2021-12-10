"""
run:
python xml_to_csv.py --type "train"
"""

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--type', help='test, val, or train',
                    required=True)
args = parser.parse_args()

image_types = ["png", "PNG", "jpg", "jpeg", "JPG", "JPEG"]

def xml_to_csv(img_files, xml_files):

    xml_list = []
    for i, xml_file in enumerate(xml_files):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            value = (img_files[i].split("/")[-1],
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member.find('name').text,
                     int(member.find('bndbox')[0].text),
                     int(member.find('bndbox')[1].text),
                     int(member.find('bndbox')[2].text),
                     int(member.find('bndbox')[3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    state = args.type
    image_path = os.path.join(os.getcwd(), ''+state).replace("\\","/")
    all_files_xml = []
    all_files_img = []
    all_path = []
    for root, subdirs, files in os.walk(image_path):
        for f in files:
            if len(files)>0:
                if f.split(".")[-1] in image_types:
                    all_files_img.append(os.path.join(root,f).replace("\\","/"))
                if f.split(".")[-1] in ["xml"]:
                    all_files_xml.append(os.path.join(root,f).replace("\\","/"))
    all_files_img = sorted(all_files_img)
    all_files_xml = sorted(all_files_xml)
    xml_df = xml_to_csv(all_files_img, all_files_xml)
    xml_df.to_csv(state+'_labels.csv', index=None)
    print('Successfully converted xml to csv.')


main()