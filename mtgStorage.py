#MTG Storage.
class card:
    def __init__(self,name,text,setcode,rarity):
        self.name=name
        self.text=text
        self.setcode=setcode
        self.rarity=rarity
    def stupid(self):
        print(self.name)
hi=card("me","knew","here","ok")
hi.stupid()