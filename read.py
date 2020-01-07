#read two integer and print  two lines. the first line should contained integer devision ,// and other line should contain float devision
a=input("enter first number = ")
b=input("second number  = ")

 # integer devision 
integer_result=int(a)//int(b)
print("integer_result =", integer_result)

# float devision
float_result=int(a)/int(b)
print("float_result =",float_result)




# same program in single line 
a,b=(input("enter two number")).split(",")
c=int(a)//int(b)
print("integer",c)
c=int(a)/int(b)
print("float",c)