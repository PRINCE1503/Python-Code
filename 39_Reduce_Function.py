# Reduce Function
from functools import reduce
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x, y: x+y, integers)
print(f"The sum of first 10 Integers is {sum}.")
