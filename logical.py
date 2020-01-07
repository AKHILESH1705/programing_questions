# AND both condition should be true
# OR only one condition should be true
# NOT revert the original value 

good_skill = True
good_communication =  True
if good_communication and good_skill:
    print("you are eligible")
else:
    print("not eligible")


good_communication = True
good_skill = False
if good_communication or good_skill:
    print("eligible")
else:
    print("not eligible")    
