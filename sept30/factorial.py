num = int(input("Enter the number:"))
fact = 1
if num<0:
    print("Wrong input")
elif num==0:
    print("Factorial of 0 = 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("factorial of",num,"is",fact)

    
