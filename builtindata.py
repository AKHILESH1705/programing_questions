""" built -in function that means predefined function or pre-defined datatype
1) none 
2) numeric data type = int, float, complex( combination of real and imaginary number like 3+4i here  3 is real number and 4i is imaginary part )
3) sequences : string, list, bytes,bytearray , tuple , range 
4) bool type represent bollean value TRUE and FALSE
5)sets
6)mappings(dictionary)
7) frozenset

"""

#1 none contain nothing and its note same as zero because zero hase some objectid or value 

a=None
print(type(a)) # type function shows its class and object = NoneType

#2 numeric datatype
#a) integer data type  occuipied 4 byte memory and there is no range in python 
a=int(50)
print(type(a))# in python we dont need  to define data type 

#b)float data type stores floating data value like (12.05) and float datatype occupied  8 byte of memory 

b=float(12.02)
print("b :",type(b))# type is function that shows class float 

#c) complex data type  combination of real and imaginary number ex: 3-5j there 4 is real number and 5j is imaginary number value of j is square root of -1 (-1)^0.5
a=3+5j
b=5-3j
print("result ",a+b)



