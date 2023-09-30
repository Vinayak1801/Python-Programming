year1=int(input("Enter year1:"))
year2=int(input("Enter year2:"))
for i in range(year1,year2):
    if(i%400==0) or (i%4==0 and i%100!=0):
        print(i, "is leap year")
