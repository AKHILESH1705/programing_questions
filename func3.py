def Greater_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2  
    else:
        return num3
a=int(input("enter first number = "))       
b=int(input("enter second number = "))   
c=int(input("enter third number = "))   

greatest=Greater_number(a,b,c)
print(f"{greatest} is greater ")