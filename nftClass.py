from os import getcwd
from pathlib import Path


class NFT:
    def __init__(self , name , description , metadata , file):
        self.name = name
        self.description = description
        self.metadata = metadata
        self.file = file
        
path = Path(getcwd())
print(path)