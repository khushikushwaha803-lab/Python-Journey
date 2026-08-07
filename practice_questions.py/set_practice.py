#how can we form a set while running program ?
choice="Y"
mylist=set() #to craete a blank set
while(choice=="Y"):
    location=input("Enter Location : ").strip().title()
    mylist.add(location)    
    choice=input("Wnat to Add Another Location ?").strip().upper()
    if(choice=="Y"):
        continue
    else:
         break

print("List of All Locations")
print(mylist)    