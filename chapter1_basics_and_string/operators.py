a=int(input("eneter the number: "))
b=int(input("eneter the number: "))
#arithmetic operators
print(a+b)    #sum operators
print(a-b)    #subtraction operator
print(a*b)    #multiplication operator
print(a/b)    #division operator
print(a//b)   #floor division operator (avoid float values)
print(a%b)    #modulus operator (remainder)
print(a**b)   #exponential operator

#comparision operators

print(a>b)   #greater than
print(a<b)   #less than
print(a>=b)  #greater than equal to
print(a<=b)  # less than equal to
print(a==b)  #equal to
print(a!=b)  #not equal to

#logical operator

print(a==1 and b==1)
print(a>5 or b<5)   
print(not(a==3))

#membership operator

fruits=["apple","orange","lichi"]
print("apple" in fruits)      #present
print("grapes" not in fruits)  #not present

#identity operator
c=34
d=30
e=30
print(c is d)     #same object
print(c is not d)   #not same object
print(d is e)       #same object


