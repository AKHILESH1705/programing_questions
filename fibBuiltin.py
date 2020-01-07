# builtin python tool
from functools import lru_cache
@lru_cache(maxsize = 1000)

def fiboacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fiboacci(n-1) + fiboacci(n-2)
for n in range(1,100):
    print(n,":",fiboacci(n)) 