#This program takes the marks of a student as input and prints the corresponding grade based on the marks.
marks=int(input("enter the marks of students:"))
if(100>=marks>=90):
    print("excellent")
elif(90>marks>=80):
    print("A")
elif(80>marks>=70):
    print("B")
elif(70>marks>=60):
    print("C")
elif(60>marks>=50):
    print("D")
else:
    print("F")     