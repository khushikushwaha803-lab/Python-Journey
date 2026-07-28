t=(1,2,32,"geetanjali",3.2,4.5) #collection of different datatypes like list

tuple=(21,32,43,54,2,3.2)
print(tuple)

print(t[0])  #retriving element of zero index

print(t.count(2)) #count the ocuurence of number 2

print(t.index("geetanjali")) #figure out the index of element

print(t[1:4]) # slicing in tuples
print(t)

print(sum(tuple)) #sum of all the elements in the tuple

print(max(tuple))  #max value among all the data in tuple

print(min(tuple))   #min value among all the data in tuple

print(len(tuple))   #finds no. of elements in the tupple
 
print(sorted(tuple)) #sort the items of the tuple

print(t+tuple)  #concatenate two tuples