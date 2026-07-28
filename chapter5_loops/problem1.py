#to print multiplication table of a number using for loop
n=int(input("enter the number"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

#using while loop
i=0
while(i<10):
    i+=1
    print(f"{n} * {i} = {n*i}")
        
