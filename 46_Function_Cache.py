#  Function Cache
import time
from functools import lru_cache


@lru_cache(maxsize=3)
def Cache_Func(n):
    time.sleep(n*1.4)
    return n+2


a = float(input("Enter a  number for delay Output : "))
print("Function Running....")
Cache_Func(a)
print("done! Ran Successfully!")
print("Again Running.......")
Cache_Func(a)
print("done! Ran Successfully!")
