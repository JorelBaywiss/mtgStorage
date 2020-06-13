fle=open("MTG.txt","r+")
cards=fle.readlines()
fle.close()


fle=open("MTG.txt","w")
fle.write("")
fle.close()
fle=open("MTG.txt","a")
for item in cards:
    fle.write(item)
fle.close()