#program to add values during run time in a tuple 
mytuple=()   #creating an empty tuple
mylist=[]
choice="Y"
while choice=="Y":
    items=input("enter th evalue ").upper()
    mylist.append(items)
    choice=input("want to add anaother values ? : ").upper()
    if choice=="Y":
        continue
    else:
        break
mytuple=tuple(mylist) 
print("the whole tuple is as follows")
print(mytuple)   
