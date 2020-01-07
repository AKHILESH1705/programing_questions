# write a program for pattern like
"""
* * * * *
* * * *
* * *
* * 
* 
"""


num=int(input("enter number of rows : "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()    


