S=set()
print(type(S))

A=18
print(type(A))
B="18"
print(type(B))

S=set()
S.add(18)
S.add("18")
print(S)


S.add(20)
S.add(20.0)
S.add("20")
print(len(S))
