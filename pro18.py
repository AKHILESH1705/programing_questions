# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return thrice of their sum.

n1= int(input("enter number1 = "))
n2= int(input("enter number2 = "))
n3= int(input("enter number3 = "))

if n1!=n2!=n3:
    print("sum=",n1+n2+n3)
else:
    print((n1+n2+n3)*3)


# by using function 


def  sum_thrice(x,y,z):
    if x==y==z:
        return (x+y+z)*3
    else:
        return x+y+z
print(sum_thrice(1,2,3))
print(sum_thrice(3,3,3))    



# another way using function

def sum_thrice(x,y,z):
    sum=x+y+z
    if x==y==z:
        sum=sum*3
        return sum
        
print(sum_thrice(4,4,4))        

