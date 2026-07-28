#This program takes four numbers as input and determines which one is the greatest among them.
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=int(input("enter the number:"))
if(a>b and a>c and a>d):
    print("a is greater")
elif(b>a and b>c and b>d): 
    print("b is greater")
elif(c>a and c>b and c>d):
    print("c is greater ")
else:
    print("d is greater") 