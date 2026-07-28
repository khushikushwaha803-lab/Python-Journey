#greatest of three numbers using function
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
a=int(input("enter the number :"))    
b=int(input("enter the number :"))  
c=int(input("enter the number :"))  
print(f"{greatest(a,b,c)}")
    