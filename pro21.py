a=int(input("enter number : "))
b=int(input("enter number : "))
if(a>b):
    min=a
else:
    min=b
while (1):
    if(min%a==0 and min%b==0):
        print("lcm is : ",min)
        break
    min=min+1            



"""def lcm (a,b):
    temp=a
    while (temp % b)!=0:
        temp += b
    return temp    
lcm(256,2155) """   