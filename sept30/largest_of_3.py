num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if (num1>num2) and (num1>num3):
    print("num1 is bigger")
elif (num2>num1) and (num2>num3):
    print("num2 is bigger")
elif num1==num2==num3:
    print("All are equal")
elif num1==num2:
    if num3>num2:
        print(num3, "is bigger")
    else:
        print(num1," and ",num2," are bigger")
elif num3==num2:
    if num1>num2:
        print(num1," is bigger")
    else:
        print(num3, " and ",num2, " are bigger")        
else:
    print("num3 is bigger")
