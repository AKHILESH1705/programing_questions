# write program for pattern like 
"""
*
**
***
****
               """

num= int(input("enter number of row : "))
for i in range(1,num+1):# it prints row
    for j in range(1,i+1):# it prints column
        print("*",end=" ")
    print()    
