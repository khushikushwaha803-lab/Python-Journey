def sum(n):
   
   if(n==1):
    return 1
   return sum(n-1)+n
n=int(input("enter the first n natural number: "))
print(f"sum of fisrt {n} natural numbers : {sum(n)}")