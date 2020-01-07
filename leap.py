#enter a year
year=int(input("enter year="))

#check condition for leap year
if year%4==0:
    print("year is leap year")
elif year%400==0:
    print(" leap year")
elif year%100==0:
    print("leap year")
else:
    print("normal year")
    
