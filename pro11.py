#Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
#Sample function : abs()

# statement print : Return the absolute value of the argument
print(abs.__doc__)

# users have input like -28, +365 etc
number=int(input("enter an integer number: "))
print("absolute value of integer number :",abs(number))

#random floating number
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))