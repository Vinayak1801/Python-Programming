listn = ["vinayak", "shabeeb", "sanjay", "irfan", "mubaris"]
count=0
print(listn)
a = input("enter the letter required:")
for n in listn:
    for f in n:
        if f==a:
            count+=1

print("the number of",a,"is", count)
