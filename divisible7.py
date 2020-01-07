#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

nl=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))# The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator



print("..............................")





x=[]

for i in range(1,300):
    if (i%7==0)and(i%5!=0):
        x.append(i)


#we can delet element from the list after printing element usiong del method called delete method
del(x[1])
print(x)