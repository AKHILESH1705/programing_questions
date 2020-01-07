name="Akhilesh"
age="19"
#ugly fomat
print("hello " + name + " your age is  " + age)# we have to remeber that we cant add integer with string,we have give some space otherwise it seems to single sequence

#string formating using python 3 and python 3.6

age =19 
#good
print("hello {} your age is {}".format(name,age)) # string formating based on version python 3
# best  we can perform operation in braces like {age+2}
print(f"hello {name} your age is {age+2}") # here f  shows formating it based on version 3.6

print(f"hello {name} your age is {age*2}") # here f  shows formating it based on version 3.6
