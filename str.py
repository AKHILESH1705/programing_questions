# str concatenation 
first_name="akhilesh"
last_name="kushwah"

print(first_name + " " + last_name)

# if  we want to concatenate  integer number to the string then we got error like type error and we need to define integer as a "number "\

# example
#print(first_name + 3) in these case we got type error 
print(first_name + "3")
print(last_name + str(3))  
print(first_name*3)
# user input string and it only take string 

stri = input("enter string : ")
print(stri)

#one more example
num1=input("first number:  " )
num2=input("first number:  " )
# string concatenation like 5+5=55
total=num1+num2
print(total)

num1=input("first number:  " )
num2=input("first number:  " )
# we need to change it into integer  first for performing addition 5+5=10
total=int(num1)+int(num2)
print(total)