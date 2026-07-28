#farenheit to celcius conversion using function
def convert():
    celcius=5*(farenhiet-32)/9
    return celcius
farenhiet=int(input("enter the temperature : "))
c=convert()
print(f"farenheit is converted into celcius :{round(c,2)}°C")