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
        color_list=[]
        if find(manacost,"W"):
            color_list.append("W")
        if find(manacost,"U"):
            color_list.append("U")
        if find(manacost,"B"):
            color_list.append("B")
        if find(manacost,"R"):
            color_list.append("R")
        if find(manacost,"G"):
            color_list.append("G")
        if len(color_list)==0:
            self.color="Colorless"
        elif len(color_list)==1:
            self.color=color_list[0]
        else:
            self.color="Multicolored"
holder=open("MTG.txt","r+")
cards=holder.readlines()
for i in range(len(cards)):
    cards[i]=cards[i].strip("\n")
holder.close()
#Changing the cards variable
#Down below |
#           |
#           v


#           ^
#           |
#Up above   |
#Changing the cards variable
holder=open("MTG.txt","w")
holder.write("")
holder.close()
holder=open("MTG.txt","a")
for item in cards:
    print(item)
    holder.write(item)