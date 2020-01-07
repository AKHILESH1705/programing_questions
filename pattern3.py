# write a python  program for pattern like 
"""
    *    
   * *
  * * * 
 * * * *
 """
num = int(input("enter number of rows : ")) # suppose num = 4 
for i in range(0,num):# i becomes 0 to 4 that means 0,1,2,3  ,,,,,, in first i=0
    for j in range(0,num-i-1):# j becomes 0 to (4-0-1) 0,3 ,,,,,,,, spaces print three times
        print(end=" ")# end is keyword  for print blanck  space (   ) 
    for j in range(0,i):# again j execute 0,0 it will execute once and print * 
        print("*",end=" ")
    print()        


