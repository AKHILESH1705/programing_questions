#Initialize array
print('enter array element')
arr1 =[];

#create another array arr2 with size of arr1

arr2 =[None]*len(arr1)


#copying all elements of one array into another
for i in range(0,len(arr1)):

    arr2[i]=arr1[i]



    #displaying all elements off array1

    print("element of original array")
    for i in range(0,len(arr1)):

        print();
        #diplaying elements of array arr2
        print('element of neww array: ')


        for i in range(0,len(arr1)):
            print(arr2[i])
