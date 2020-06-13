from os import system
#definition of functions go here: |
#                                 v
system("cls")
def colour(mana_cost):
    #this function returns a list which is the colour of the card.
    colours=[]
    words={"W":"White","U":"Blue","B":"Black","R":"Red","G":"Green"}
    for word in words:
        if word in mana_cost:
            if not word in colours:
                colours.append(words[word])
    if len(colours)>=2:
        return("Multicolour")
    elif len(colours)==0:
        return("Colourless")
    else:
        return(colours[0])
#                                ^
#definition of functions go here:|
fle=open("MTG.txt","r+")
cards=fle.readlines()
fle.close()
#changes to the list go in here:|
#                               v

#changes to the list go here: ^
#                             |
fle=open("MTG.txt","w")
fle.write("")
fle.close()
fle=open("MTG.txt","a")
for item in cards:
    fle.write(item)
fle.close()