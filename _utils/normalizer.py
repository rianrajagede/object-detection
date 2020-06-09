"""
run:
python normalizer.py --rootdir "Prioritas 1"

result:
file xml yang merujuk ke citra yang sama akan di-merge di satu file xml
file xml & img yang duplikat akan dihapus

validation:
hasil file xml dan img harusnya totalnya sama di akhir
"""
import os
import argparse
import xml.etree.ElementTree as ET
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--rootdir', help='rootdir contains subdir of images and annots grouped by class',
                    required=True)
args = parser.parse_args()
image_types = ["png", "PNG", "jpg", "jpeg", "JPG", "JPEG"]

def mergexml(xml1, xml2):
    root1 = ET.parse(xml1).getroot()
    root2 = ET.parse(xml2).getroot()
    for ob in root2.findall("./object"):
        root1.append(ob)
    return ET.tostring(root1, encoding="unicode")

root_dir = args.rootdir

all_files_xml = []
all_files_img = []
all_path = [] # for debugging
for root, subdirs, files in os.walk(root_dir):
    for f in files:
        if len(files)>0:
            if f.split(".")[-1] in image_types:
                all_files_img.append([f, root])
            if f.split(".")[-1] in ["xml"]:
                all_files_xml.append([f, root])
    all_path +=files

all_files_xml = sorted(all_files_xml, key=lambda x:x[0])
all_files_img = sorted(all_files_img, key=lambda x:x[0])

print("Total file", len(all_path))
print("banyak file xml sebelum", len([x[0] for x in all_files_xml]))
print("banyak file img sebelum", len([x[0] for x in all_files_img]))
print("banyak file xml seharusnya", len(set([x[0] for x in all_files_xml])))
print("banyak file img seharusnya", len(set([x[0] for x in all_files_img])))
print("Preprocess...")

delete = []
f = all_files_xml[0]
for i in range(1, len(all_files_xml)-1):
    n = all_files_xml[i]
    if f[0] == n[0]:
        res = mergexml(f[1]+"/"+f[0], n[1]+"/"+n[0])
        with open(f[1]+"/"+f[0], "w") as F:
            F.write(res)
            delete.append(n[1]+"/"+n[0])
    else:
        f = all_files_xml[i]

f = all_files_img[0]
for i in range(1, len(all_files_img)-1):
    n = all_files_img[i]
    if f[0] == n[0]:
        delete.append(n[1]+"/"+n[0])
    else:
        f = all_files_img[i]

print("menemukan duplikat sebanyak", len(delete))
print("Delete Duplicate...")
# print(delete)

for d in delete:
    os.remove(d)


all_files_xml = []
all_files_img = []
all_path = [] # for debugging
for root, subdirs, files in os.walk(root_dir):
    for f in files:
        if len(files)>0:
            if f.split(".")[-1] in image_types:
                all_files_img.append([f, root])
            if f.split(".")[-1] in ["xml"]:
                all_files_xml.append([f, root])
    all_path +=files

all_files_xml = sorted(all_files_xml, key=lambda x:x[0])
all_files_img = sorted(all_files_img, key=lambda x:x[0])


print("banyak file xml setelah", len(all_files_xml))
print("banyak file img setelah", len(all_files_img))

np.savetxt("all_files_img", all_files_img, fmt="%s")
np.savetxt("all_files_xml", all_files_xml, fmt="%s")
