# Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.
def string_check(str):
    if len(str) >= 2 and str[:2]=="is":
        return str
    else:
        return "is" +str


name=input("enter name with (is)at front of the string and without (is) as you want : ")

print(string_check(name))




# another way 
def string_is(str):
    if str[:2]!="is":
        return "is"+str
    return str 
print(string_is("akhilesh"))
print(string_is("iskushwah"))  

# one more way

def str_is(str):
    if str[:2]=="is":
        return str
    return "is"+str
print(str_is("isdeepak"))
name=input("enter name : ")
print(str_is(name)) 
            