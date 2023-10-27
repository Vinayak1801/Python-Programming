list1 = [1,2,3,4,5]
a = []
print(list1)
a = list1[0]
list1[0] = list1[4]
list1[4] = a
print(list1)
