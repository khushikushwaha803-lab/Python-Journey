#repeating  practice question 4 for the list of such more censored word


import re  #for case sensitivity
words=["Donkey","Bad","ganda","BURA"]

with open("file.txt","r") as f:
    content=f.read()

# here case sensitive donkey will not accept
# newcontent=content.replace(word,"######") 


#re.INORECASE flag case sensitivity ko ignore krne ke liye use hua hai
for word in words:
   content=re.sub(word,"#"*len(word),content,flags=re.IGNORECASE)

with open("file.txt","w") as f:
   f.write(content)


f.close()