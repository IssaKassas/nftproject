from json import dump
from os import getcwd
from data import randomChoice
from metadata import template
from PIL import Image
from pathlib import Path

path = Path(getcwd())
path = path.absolute()

ASSETFOLDER = f"{path}\Assets"
OriginalFolder = f"{path}\OutputData\Images\Original"
ResizedFolder = f"{path}\OutputData\Images\Resized"
# IDCSV = f"{path}\Generate\GenerationIDs.csv"
ImageFileName = "Character"

def main(id):
    tokenid = str(id)
    print(f"Token Id{id + 1}")

    def generate_meta_data():
        metadata = template
        metadata_file_name = f"{path}\MetaData\{ImageFileName}{tokenid}.json"
        metadata[tokenid]["name"] = f"{ImageFileName}#{tokenid}"
        metadata[tokenid]["description"] = f"A handsome {ImageFileName}{id} NFT"
        metadata[tokenid]["file"] = f"{ImageFileName}{tokenid}.png"
        metadata[tokenid]["attributes"] = list()
        metadata[tokenid]["attributes"].append(
            {
                'Background': randomChoice()[id][0],
                'Body': randomChoice()[id][1],
                'Eyes': randomChoice()[id][2],
                'Mouth': randomChoice()[id][3],
                "Accessory": randomChoice()[id][4]
            }
        )
  
        keys = list(metadata.keys())
        for key in keys:
            new_key = key.replace(tokenid , str(id + 1))
            if new_key != key:
                metadata[new_key] = metadata[key]
                del metadata[key]
                
        with open(metadata_file_name , "w") as file:
            dump(metadata , file)
    
    generate_meta_data()
    
    baseBG = Image.open(rf"{ASSETFOLDER}\Background\{randomChoice()[id][0]}.png")
    imgBody = Image.open(f"{ASSETFOLDER}\Body\{randomChoice()[id][1]}.png")
    imgEyes = Image.open(f"{ASSETFOLDER}\Eyes\{randomChoice()[id][2]}.png")
    imgMouth = Image.open(f"{ASSETFOLDER}\Mouth\{randomChoice()[id][3]}.png")
    
    global imgAccessories
    imgAccessories = None
    
    if len(randomChoice()[id][4]) != 0:
        imgAccessories = Image.open(f"{ASSETFOLDER}\Accessories\{randomChoice()[id][4]}.png")
    
    baseBG.paste(imgBody, (0, 0), imgBody)
    baseBG.paste(imgEyes, (0, 0), imgEyes)
    baseBG.paste(imgMouth, (0, 0), imgMouth)
    
    if len(randomChoice()[id][4]) != 0:
        baseBG.paste(imgAccessories, (0, 0), imgAccessories)
        
    resized_img = baseBG.save(f"{OriginalFolder}\{ImageFileName}_{tokenid}.png", 'png', quality = 95)
    resized_img = baseBG.resize((300, 300), resample = Image.NEAREST)
    resized_img.save(f"{ResizedFolder}\{ImageFileName}_{tokenid}.png", "PNG")
