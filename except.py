# understanding exception handling in python  there are three case 
# when there  is an exception , PVm weill diosplay Exception message 
# and terminates the program abnormaly
# due to abnormal termination the files and databases are not closed hence the user data will be lost some time the entire program will crash 
# for handling exception programmer should do the following task =====
#1.==== we should write all the program statement inside the ( try: block ) 
# try block prevents abnormal program termination and our program will not terminate if its written inside try block 
# 2.==== when there is an exception in try block the pvm will jump into the  except block 
# the programmer should display exception mesage and  other messsage to the user in the except block 
# the programmer should close all the files and databases in the finally block 
# 3.===finally block is always executed when there is an exception or not
# doing the complete three task is called exception handling 
# every exception is class 

print("opening process")
a,b=input("enter value of a and value of b ").split()

try:
    c=int(a)/int(b)
   

except Exception:
    print("invalid input ")

else:
    print("result ", c)
finally:
    print("process close")

    