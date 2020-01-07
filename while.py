# aks a user for name  
#  example  akhilesh kushwah
# print count of each words
# output :
        # a: 2
        # k: 2
        # h: 4
        # i: 1
        # l: 1
        # e: 1
        # s: 2
        #  : 1
        # u: 1
        # w: 1
name=input("enter name = ")    
# i = 0 because indexing start from 0      
i=0
temp=""
while i<len(name): # len function count lenth of string and goes upto the users input string lenth
    if name[i] not in temp:# name[i] i shows indexing number 
        temp += name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i +=1        
