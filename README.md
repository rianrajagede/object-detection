# Object detection tutorial (Work in Progress)

This repo contains scripts for object detection task. Some tutorials written in Bahasa Indonesia available in [my blog](https://structilmy.com).

### Useful scripts:

1. `xml_to_csv.py`: convert PASCAL xml format to csv 
2. `generate_labelmap.py`: generate label_map.pbtxt
3. `generate_tfrecord.py`: generate tfrecord file
4. `normalizer.py`: if your subfolder format is grouped by classes. this script merge two same image with different xml files
5. `folder_check.py`: will raise an error if there are folder that contains different number of image and xml files
6. `Explorer.ipynb`: to analyze the dataset

### Tutorial:

1. `Detectron.ipynb`: A simple tutorial of object detection using [Facebook Detectron2 Framework](https://github.com/facebookresearch/detectron2)

### Dataset:

I combine and modify Raccoon and Kangaroo dataset by [Experincor](https://experiencor.github.io/). Datasets are available [here](https://github.com/experiencor/raccoon_dataset) and [here](https://github.com/experiencor/kangaroo). Thank You!




