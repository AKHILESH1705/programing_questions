 # Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)
# example Output : The examination will start from : 11 / 12 / 2014




# first logic
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

# second logic this one is my logic
date,month,year=input("enter date month year : " ).split(",")
print("%s / %s / %s"%(date,month,year))