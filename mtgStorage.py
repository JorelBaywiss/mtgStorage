#MTG Storage.
from os import system
def find(a,b):
    c=False
    for item in a:
        if item==b:
            c=True
    return c
class card:
    def __init__(self,name,manacost,text,setcode,rarity):
        self.name=name
        self.manacost=manacost
        self.text=text
        self.setcode=setcode
        self.rarity=rarity
        #color
