def Binary_search(seq,key):
    first = 0
    last = len(seq) - 1
    
    while last >= first:
        mid = first + (last-first)//2
        if seq[mid] < key:
            first = mid + 1
        elif seq[mid]> key:
            last = mid - 1
        else:
            return mid
    return False
sequence = [0,1,2,8,13,17,19,32,42]    
print(Binary_search(sequence,4))            