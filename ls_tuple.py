# Python program to sort a list of tuples by second Item 
  
# Function to sort the list of tuples by its second item 
def Sort_Tuple(tup):  
      
    # getting length of list of tuples 
    lst = len(tup)  
    for i in range(0, lst):  
          
        for j in range(0, lst-i-1):  
            if (tup[j][1] > tup[j + 1][1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp  
    return tup  
  
# function calling and input
tup =[('of', 24), ('is', 10), ('yashwant kushwah', 28),  
      ('akhilesh kushwah', 5), ('son ', 20), ('a', 15)]  
        
print(Sort_Tuple(tup)) 
print(len(tup))





#========================================================================



# Function to sort hte list by second item of tuple 
def Sort_Tuple(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    tup.sort(key = lambda x: x[1])  
    return tup  
  
# Driver Code  
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]  
  
# printing the sorted list of tuples 
print(Sort_Tuple(tup))




