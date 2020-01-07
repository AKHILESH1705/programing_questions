""" byte data type can not be modified it is similar to array byte number are positive or integer
range of bytes data type is 2^8=256 and from 0 to 255"""


b=bytes([1,2,3,4,5])
print(b)

a=b[0]#  indexing 
print(a)
for i in b :print(i)


"""b.remove[3]  there is error like attribute error no remove operaion possilbe"""
print(b)

# bytearray  data type is also there  and same as byte but the diffrence is bytearray can be modified """

ba=bytearray(b)#changing method for  changing bytes into bytearray"""
print(ba)

ba.append(1)
print(ba)

b=bytes(ba)
print(b)