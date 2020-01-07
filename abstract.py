"""A class with one or more abstract method is called abstract class to create  an object for Abstract class we have to create sub class """


from abc import ABC # importing module from 

class Myclass(ABC):
    def display(self):
        print("this is concrete method ")

def calculate(self,x):
    pass

class sub1(Myclass):# subclass 1 drived from concrete class 
    def calculate(self,x):# self represent 
        print("squre value =",x*x) 

import math
class sub2(Myclass):# subclass2 drived from concrete class
    def calculate(self,x):
        print("square root =",math.sqrt(x))

s1=sub1()
s1.calculate(16)

s2=sub2()
s2.calculate(16) 