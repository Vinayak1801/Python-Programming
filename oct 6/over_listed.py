list1=int(input("enter the limit:"))
i = 0
list2 = []
while i<list1:
    z = int(input("enter the number:"))
    if z>100:
        list2.append("over listed")
    else:
        list2.append(z)
    i+=1

print(list2)
