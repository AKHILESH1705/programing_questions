num=int(input("enter number:"))
i=2
toggle=0
while i<num:
    if num%i==0:
        flag=1
        print("you no. is not prime")
        print(i,"times",num//i,"is",num)
        break
    i=i+1

if flag==0:
    print("your no. is prime number.")
    

        
            
          
        
            


             
