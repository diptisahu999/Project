import os

directory = './dump/ABC_tbl/'
files = os.listdir(directory)

for file in files:
    if file.endswith('.json'):
        filepath = os.path.join(directory, file)
        os.system(f"mongoimport --db mydb --collection BMS_v2 --file {filepath}")