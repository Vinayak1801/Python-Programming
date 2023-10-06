a=input("enter the sentence")
b=input("type the word to search")
lit = a.split()
count=0
for n in lit:
    if n==b:
        count+=1

print("the number of", b , "is", count)
