nums = [10,20,30,40,50]

for num in nums:
    if num % 7 ==0:
        print(num)
        break # for terminating loop if we want all the number then we have to remove break  
else: # else part will be in the body of for loop other wise it will execute many times depend on len of list 
    print("not found")

