#Memoization
# two way of memoization 
# 1) Implement explicitly
# 2) Use builtin Python tool 
#idea: Cache values


fiboacci_cache = {}
def fiboacci(n):
    if n in fiboacci_cache:
        return fiboacci_cache[n]
    # compute the nth term 
    if n ==1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value=fiboacci(n-1)+fiboacci(n-2)
    fiboacci_cache[n] = value
    return value
for n in range(1,10):
    print(n,":",fiboacci(n))

       