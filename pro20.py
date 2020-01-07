#Write a Python program to get a string which 
# is n (non-negative integer) copies of a given string.

def string_copies(str,n):
    result=""
    for i in range(n):
        result=result+str
    return result
print(string_copies("akhi",2))


# another way
def str_copies(text,n):
    return (text * n)
text=input("enter text : ")
n=int(input("enter repitation time : "))

print(str_copies(text,n))


# one more 

def copies(text ,n):
    return (text*n)
print(copies("akhi",3))    
