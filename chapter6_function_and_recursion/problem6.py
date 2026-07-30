def remove(l,word):
    new_list=[]
    for item in l:
        if not(word==item):
           new_list.append(item.strip(word))
    return new_list

l=["anjali","rohan","preeti","gungun"]
print(remove(l,"an"))

