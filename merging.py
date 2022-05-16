import json
from os import getcwd, listdir , path
from pathlib import Path
from jsonClass import JSON

paths = Path(getcwd())
folder = f"{paths}\Metadata"

files = []
for f in listdir(folder):
    if path.isfile(path.join(folder , f)):
        files.append(f)
        
def merge_json(filename):
    result = list()
    for f in filename:
        with open(path.join(folder , f) , "r") as file:
            result.append(json.load(file))
    
    with open(f"{paths}\OutputData\metadata.json" , 'w') as output_file:
        json.dump(result , output_file)

merge_json(files)

file = JSON(f"{paths}\OutputData\metadata.json")

file = file.reader()

for data in file:
    for key in data:
        name = data[key]['name']
        description = data[key]['description']
        file = data[key]['file']
        metadata = data[key]['attributes']
        print(name , description , file , metadata)