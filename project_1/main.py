#"Snake,Water,Gun Game using nested if"


import random
""" snake=1
    water=-1
    Gun=0
"""
computer=random.choice([1,-1,0])
your_choice=input("enter your choices : ").lower().strip()
dict={"s":1 , "w":-1 , "g":0}
reverse_dict={1:"snake" , -1:"water" ,0:"gun"}

you=dict[your_choice]

print(f"your choice is {reverse_dict[you]} \ncomputer's choice is {reverse_dict[computer]}")

if(computer==you):
    print("game is draw")
else:    
    if(computer== 1 and you== -1):
        print("you loose")
    elif(computer== 1 and you== 0):
        print("you win")
    elif(computer== -1 and you== 1):
        print("you win")       
    elif(computer== -1 and you== 0):
        print("you loose") 
    elif(computer== 0 and you== 1):
        print("you loose")
    elif(computer== 0 and you== -1):
        print("you win")    
    else:
         print("something went wrong")              

