n=int(input("enter the first n natural numbers:" ))
i=0
product=1
for i in range(1,n+1):
    product=product*i
    i=+1
print(f"factorial of number{n}is{product}")    

