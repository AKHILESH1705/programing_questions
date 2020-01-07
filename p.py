print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, trinagle of odd numbers\n ")

num = int(input(" enter  number of row :"));print(" ")
k=1
for i in range (1,num+1):
    for j in range (1,k+1):
        print("*",end=" ")
    k+=2 
    print()   


print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,triangle\n")


num = int(input("enter number of row : "));print(" ")
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    

print('""""""""""""""""""""""""""""""""""""""""""""""reverse pyramid\n')

num = int(input("enter number of row : "));print(" ")
for i in range (num,0,-1):
    for j in range (0,num-i):
        print(end=" ")
    for j in range (0,i):
        print("*",end=" ")
    print()        


print("...................................................................................... pyramid\n")


num= int(input("enter number of rows : "));print(" ")# num = 4
for i in range (0,num):#0,1,2,3
    for j in range(0,num-i-1):#0,4-0-1=3,0,1,2 three spaces it will print 
        print(end=" ")
    for j in range(0, i+1):# after condition false 0, 0+1=1 >  0,1     
        print("*",end=" ")# it will execute onece only,,,,,,,, 
    print()


print("..............................................heart shape\n")   

for row in range(0,6):
    for col in range(0,7):
        if(row==0 and col%3!=0) or (row==1 and col%3==0) or(row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()


print("...............................................................................\n square shape\n ")

num=int(input("enter number of rows : "));print(" ")
for i in range(0,num):
    for j in range(0,num):
        print("*",end=" ")
    print()
            
print(".............................................\n print reverse of triangle\n")

num = int(input("enter number of rows : "));print(" ")
for i in range(0,num):
    for j in range(0,num-i):
        print("*",end=" ")
    print()  

print(".........................................\n print letter A\n")

for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0) or((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()            



print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, \n print letter B\n")

    






















