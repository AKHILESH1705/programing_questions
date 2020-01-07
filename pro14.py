""" Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)"""


from datetime import date

date_f=date(2015,7,2)
date_l=date(2016,7,11)

delta = date_l-date_f

print(delta.days)