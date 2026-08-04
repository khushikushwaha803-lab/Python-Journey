# A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ##### by updating the same file.


import re  #for case sensitivity
word="Donkey"

with open("file.txt","r") as f:
    content=f.read()

# here case sensitive donkey will not accept
# newcontent=content.replace(word,"######") 


#re.INORECASE flag case sensitivity ko ignore krne ke liye use hua hai

newcontent=re.sub(word,"######",content,flags=re.IGNORECASE)

with open("file.txt","w") as f:
   f.write(newcontent)


