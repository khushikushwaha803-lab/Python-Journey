#salary slip of the employee
while True:
    empname=input("enter the name of the employee : ").upper().strip()
    if(len(empname)==0):
       print("sorry name is blank")
       continue
    else:
       break
while True:    
    salary=int(input("enter salary : "))
    if(salary<25000):
       print("sorry salary cannot be less than 25000")
       continue
    else:
     bonus=salary*.3
     break
print("NAME\t\t\tSALARY\t\tBONUS")
print("****\t\t\t******\t\t*****")
print("%s\t\t%.2f\t\t%.2f" %(empname,salary,bonus))