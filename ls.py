#  list is data type  and can be modified 
#del(),append(),index(),nesting(()),remove(),pop(),extend

ls=[5,5,6,4,5,6,123,1,7]

ls.append(55555)# to add any number any character to the list we can use append method 
print(ls)

del(ls[1])# Del fubnction delete element to the indexing 
print(ls)

ls.remove(123)# remove method remove  perticular element 
print(ls)

la=[1,2,3,4,5,[1,2,3]]# nesting in  list 
print(la)

print(la[0:5])# starting point is 0 and end point is 5 so 5-1 = 4 internally and print  list from 0 to 4.

print(la[-1::-2]) # this is steping if we can not give step size then by default is 1 and no skip if we give 2 then skip 2 element 

# other example of list slicing 
ls1=[1,2,3,5,[1,2,3],{1:'akhilesh',2:'kushwah',3:'chotu'},('a','b','b')]


print(ls1[5])


a=ls1[5][2]
del(ls1[5][2])
print(ls1)

#del(ls1[6][1])  # error because tuple doesn't support deletion because of its immutibale nature 
#print(ls1)


#ls1.remove(6)# error because tuple doesn't support deletion because of its immutibale nature
#print(ls1)

#print(ls1.index(6))# any element doest not exist in the list then the error is called   valueError 


print(ls1.index(1))# index method gives the position of index

list1 = [ 1, 2, 3, 4, 5, 6 ] 
  
# Pops and removes the last element from the list 
print(list1.pop(),list1) 


print(ls1.pop(2),ls1) 


list2=[6,7,9,10,11,12,13,14]

list2.extend([1])# extend method take multiple element in the form of list and add as a individual element 
print(list2)

list2.append([123,5,'Akhilesh'])# append method add element as a single element 
print(list2)



# update list 
lis=['akhilesh',"kushwah",['prince',"verma"],("a",'b',"c")]

lis[3]={'a':1}
print(lis)



# sorting is an technique  to sort the element of list in accending order 


la=[40,50,61,12,1,2,8,3,4,56,78,4,7,500,60,13,15,19]
la.sort()
print(la)


# sorting in decending order 

la.sort(reverse=True)
print(la)

