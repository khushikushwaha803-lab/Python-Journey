f=open("file.txt")
print(f.read())
f.close()

#the same can be done as using with function
with open("file.txt") as f:
    print(f.read())

#there is no need to close the file explicitly    