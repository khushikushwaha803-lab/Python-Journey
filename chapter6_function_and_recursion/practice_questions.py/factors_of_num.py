num=int(input("enter the number:"))
print("list of the factors are: ")
for x in range(1,num+1):
    result=num%x
    if(result==0):
        print(x)
print("end of program")  