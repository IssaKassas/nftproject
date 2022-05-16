from json import load

class JSON:
    def __init__(self , filename):
        self.filename = filename
        
    def reader(self):
        return load(open(self.filename))
    