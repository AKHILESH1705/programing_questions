import calendar 
# checking whether given year is leap or not 
print(calendar.isleap(2016)) 
print(calendar.isleap(2001)) 

# print april month
import  calendar
y=2014
m=4
print(calendar.month(y,m))

# importing calendar module  
import calendar  
    
text_cal = calendar.TextCalendar(firstweekday = 30)  
    
year = 2018
width = 4
    
# printing pryear 
print(text_cal.pryear(year, width))   