# Write a Python program to accept a filename from the user and print the extension of that.
# example input=function.py , output=py

filename=input("enter user name : ")
file_extension=filename.split(".")
print("extension of file is " + repr(file_extension[-1]))




# one more way 

filename=input("enter file name  : ")
filename=filename.split(".")[-1]
print(" file extension = ",filename)