sum=0
print("Enter the numbers:")
lim = int(input())
print("Enter ",lim," Numbers:")
for i in range(lim):
    lim = int(input())
    sum = sum+lim
    avg = sum/lim
print("Sum of given numbers:", sum)
print("Average of given numbers: ",avg)
