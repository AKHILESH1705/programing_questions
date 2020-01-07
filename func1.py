# function for check odd or even number
def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print("num=",even_odd(5)) 



# diffrent way to find even odd
def odd_even(num1):
        if num1%2==0:
            return "even"
        return "odd"    
print(odd_even(4))    



# one more way
def is_even(num2):
    if num2%2==0:
        return True
    else:
        return False 
print(is_even(3))      


# check even odd 
def even_is(num3):
    return num3%2==0
print(even_is(4))   


# without passing parameter
def song():
    return "happy birthday akhilesh"

print(song())