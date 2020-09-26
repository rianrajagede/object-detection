"""
run:
python splitter.py --rootdir "Prioritas 1"

result:
akan membuat folder train, val, test dengan banyak data masing-masnig:
test = 2 image untuk setiap label
val = 20% dari total data - test
train = 80% dari total data - test
"""
import os
import argparse
from shutil import copyfile

parser = argparse.ArgumentParser()
parser.add_argument('--rootdir', help='rootdir contains subdir of images and annots grouped by class',
                    required=True)
parser.add_argument('--test', help='between 0-1 proportions of test set',
                    default=0.1, type=float)
parser.add_argument('--val', help='between 0-1 proportions of validation set',
                    default=0.1, type=float)
args = parser.parse_args()

root_dir = args.rootdir
test_size = args.test
val_size = args.val

all_files_xml = []
all_files_img = []
all_path = []
for root, subdirs, files in os.walk(root_dir):
    for f in files:
        if len(files)>0:
            if f.split(".")[-1] in ["png", "jpg", "jpeg"]:
                all_files_img.append(os.path.join(root,f))
            if f.split(".")[-1] in ["xml"]:
                all_files_xml.append(os.path.join(root,f))
    all_path +=files

all_files_xml = sorted(all_files_xml)
all_files_img = sorted(all_files_img)

print("Total file", len(all_path))

if not os.path.exists("train/"):
    os.mkdir("train/")
if not os.path.exists("val/") and val_size > 0:
    os.mkdir("val/")
if not os.path.exists("test/") and test_size > 0:
    os.mkdir("test/")

for root, subdirs, files in os.walk(root_dir):
    if root!=root_dir:
        print("Splitting", root)

        T = int(len(files)//2*test_size) # test size
        V = int(len(files)//2*val_size) # val - percentage
        L = len(files)//2-T-V # all - test

        all_files_xml = []
        all_files_img = []
        
        for f in files:
            if f.split(".")[-1] in ["png", "jpg", "jpeg"]:
                all_files_img.append(os.path.join(root,f))
            if f.split(".")[-1] in ["xml"]:
                all_files_xml.append(os.path.join(root,f))
        
        all_files_xml = sorted(all_files_xml)
        all_files_img = sorted(all_files_img)

        for i,x in zip(all_files_img[:T], all_files_xml[:T]):
            copyfile(i,"test/"+i.split("/")[-1])
            copyfile(x,"test/"+x.split("/")[-1])
        
        for i,x in zip(all_files_img[T:T+V], all_files_xml[T:T+V]):
            copyfile(i,"val/"+i.split("/")[-1])
            copyfile(x,"val/"+x.split("/")[-1])
        
        for i,x in zip(all_files_img[T+V:], all_files_xml[T+V:]):
            copyfile(i,"train/"+i.split("/")[-1])
            copyfile(x,"train/"+x.split("/")[-1])
