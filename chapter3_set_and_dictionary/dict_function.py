dict={ "name" : "geetanjali",
      "course" : "btech",
      "age" : 21,
      "DOB" : 23,
      "semester": "seventh"
}
print(dict) #printing the dictionary

print(dict.items()) #printing the items of the dictionary

print(dict.values()) #printing the values of the dictionary

print(dict.keys()) #printing the keys of the dictionary

dict.update({"age":20}) #updating the value of the key "age" in the dictionary

print(dict)

dict.update({"cgpa":8.432})

print(dict)

dict.pop("age") #removing the key "age" and its value from the dictionary
print(dict)
print(dict.get("name")) #getting the value of the key "name" from the dictionary

print(dict["name"]) #getting the value of the key "name" from the dictionary

print(dict["age"]) #getting the value of the key "age" from the dictionary

dict.setdefault("year", 2023) #setting a default value for the key "year" in the dictionary
print(dict)

dict2=dict.copy() #copying a dictionary into another dictionary
print(dict2)

dict2.clear() #clearing the dictionary
print(dict2)

keys={"geetanjali","age","DOB"}
newdict=dict.fromkeys(keys,"none") #creating a new dictionary with keys from the set and default value "none"
print(newdict)