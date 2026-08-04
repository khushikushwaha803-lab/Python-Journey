#print Tables from 1 to 20
def table_generator(n):
    # print(f"\nTable of {i}")
    table=""
    for i in range(1,11):
        result=n*i
        table+=f"{n}*{i}={result}\n"
        table = table.rstrip("\n") 

    with open(f"tables/table_{n}.txt","w") as f:
      f.write(table)

for i in range(2,21):
   table_generator(i)