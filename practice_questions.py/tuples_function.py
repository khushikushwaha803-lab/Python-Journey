#performimg functions on Tuples
stationlist=("New Delhi","Amritsar","Mughal Sarai","Lucknow","Jaipur","Hyderabad","Itarsi","Nagpur")
newname=[]
for x in stationlist:
    if(x=="Mughal Sarai"):
        x="DDU Station"
        newname.append(x)

    else:
        newname.append(x)

stationlist=tuple(newname)     
print("updated station list=")
print(stationlist)  

print(sorted(stationlist,reverse=True))