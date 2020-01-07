# Write a Python program to get the difference between a given number
# and 17, if the number is greater than 17 return double the absolute difference.


def diff(n):
  if n <=17:
    return abs(n-17)
  else:
    return (n-17)*2

print(diff(22))

print(diff(14))