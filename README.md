# Object detection scripts

This is my personal script for future usage. Some tutorials available in my blog.

Explanation how to run each script included in each file.
Order to run:

1. `xml_to_csv.py` to convert xml to csv 
2. `generate_labelmap.py` to generate label_map.pbtxt
3. `generate_tfrecord.py` to generate tfrecord file

Explanation of other scripts:

1. `normalizer.py`: if your subfolder format is grouped by classes. this script merge two same image with different xml files
2. `folder_check.py`: will raise an error if there are folder that contains different number of image and xml files
3. `Explorer.ipynb`: to analyze the dataset

