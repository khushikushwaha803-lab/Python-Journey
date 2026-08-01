f=open("poems.txt")
data=f.read()
if("twinkle".upper() in data):
  print("the word twinkle is present")
else:
  print("the word twinkle is not present")  

f.close