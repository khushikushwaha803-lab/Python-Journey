A={23,45,2,30,90,66,1}
B={23,2,30}

C=A.union(B)  #union of two sets
print(C)

I=A.intersection(B)  #intersection of two sets
print(I)

A.add(10) #adding an element to the set
print(A)

print(A.difference(B)) #difference of two sets

print(B.issubset(A))  #checking if B is a subset of A

print(A.issuperset(B))  #checking if A is a superset of B

print(A.isdisjoint(B))  #checking if A and B are disjoint

A.remove(23) #removing an element from the set
print(A)

A.discard(2)  #discarding an element from the set
print(A)

A.discard(2) #discarding an element from the set which is not present in the set
print(A)
 
C=A.copy() #copying a set into another set
print(C)

A.pop()  #removing an arbitrary element from the set
print(A)
 
A.remove(2) #removing an element from the set which is not present in the set
print(A)