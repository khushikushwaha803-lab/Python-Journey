#greet all the person in the list name starts with S
L=["geetanjali","sakshi","gunnu","saurabh","shushsu"]
for name in L:
# name=0
# while(name<len(L)):
#     name+=1
    if(name.startswith("s")):
        print(f"Good morning {name}")
