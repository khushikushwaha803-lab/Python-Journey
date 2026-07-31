#Data cleaning using strng slicing
procode="LEN/EN/MAR-PS8890"
#thier purpose is to encrpt this data in the given form
#"LEN/EN/MAR-PS8XXX"
newprocode=procode[0:len(procode)-3]
newprocode+="XXX"

print("Encrpted code=",newprocode)

#thier purpose is to encrpt this data in the given form
#"LEN/EN/MAR-XXX890"

part1 = procode[0:11]      
part2 = "XXX"              
part3 = procode[14:]        

newprocode = part1 + part2 + part3
print(newprocode)   

#using spilt function
newcode=procode.split("-")
newstring="XXX"+newcode[1][3:len(newcode[1])]
print(newcode[0]+"-"+newstring)