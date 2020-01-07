# fibonacci series  like 0 1 1 2 3 5 8 13 21 34 55
def fibonacci_seq(n):
    a=0
    b=1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b, end= " ")
        for i in range(n-2): # when we pass n=8 it goes upto 10 so we have to Define(n-2)
            c= a + b
            a = b
            b = c
            print(b,end = " ")
fibonacci_seq(8)