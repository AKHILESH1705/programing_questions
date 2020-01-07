# string is group of character 

name=input("enter your name :   ")
print("name  ===",name )




# indexing retrieving element by its position 
print(len(name))
print(name[0:3])#if we put[start point(default value is starting of string ) : end point(default value is last position of string ) ]

# string slicing retrieving a range of element there  are step [starting point : end point : steps for skiping character]
print(name[::-1])# print reverse of string 

print(name[5::2])# starting from fifth position and ending at default , step of 2 that means skip element and print output 



print(name[8::-1]) # same as above 

# repetition of string 

print(name*2) # it will print two time 

