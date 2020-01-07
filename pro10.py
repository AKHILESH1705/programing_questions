# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.


# this my logic
N=input("enter number : ")
ANSWER=int(N)+int(N*2)+int(N*3)

print(ANSWER)

print(type(ANSWER))# class int

# this is another logic
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
N=n1+n2+n3


print(type(N)) # class = int

