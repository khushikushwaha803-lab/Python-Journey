list=[1,"geetanajlai","faridabad",21,8.432]
print(list.append("intelligent")) #add the element at the last index of the  list
print(list)
print(list.remove(21)) #remove the element from the list
print(list)
print(list.pop(2)) #delete the element with the help of indexing
#creating list2
list2=[1,32,455,54.3,2,299]
print(list2)

list.extend(list2) #concatenate the two lists
print(list)

list3=list.copy() # copy one list into another
print(list3)

list.count(2) # count the occurence of the element
print(list2)

print(list2.sort()) # sort the list in ascending order
print(list2)

list.insert(1,"guunuu") # insert the element in the list with the choice of index
print(list)

list2.reverse()  # reverse the list
print(list2)

print(list2[1:4]) #slicing in list

print(list.index(1)) #return the index of the data

list2.clear() # clears the existing list
print(list2)


