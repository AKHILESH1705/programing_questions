# Next: Write a Python program to test whether a number is within 100 of 1000 or 2000.

def check(num):
    return 1000-num<=100 or 2000-num<=100

print(check(800)) 
print(check(1200))   
    
