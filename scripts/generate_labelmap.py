"""
run:
python generate_labelmap.py

required train_labels.csv, it assumes all labels are included in data train
"""

import pandas as pd

df = pd.read_csv("train_labels.csv") # asumsi label paling lengkap
idx = 1
dic = {}

with open("label_map.pbtxt", "w") as f:
    for idx, label in enumerate(df["class"].unique()):
        idx+=1
        f.write("item{\n")
        f.write("id: %d\n" % (idx))
        f.write("name: '" + label + "'\n")
        f.write("}\n\n")

print("DONE")