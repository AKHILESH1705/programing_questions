#cheack which number is greater
def number(num1,num2):
    if num1>num2:
        return a
    else:
        return b
a=int(input("enter num1 = "))
b=int(input("enter num2 = "))

bigger=number(a,b)

print(f"{bigger} is greater")



# diffrent way

def number(num1,num2):
    if num1>num2:
        return "num1 is greater"
    else:
        return "num2 is greater"
a=int(input("enter num1 = "))
b=int(input("enter num2 = "))

print(number(a,b))