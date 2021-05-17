# Comprehensions

# List Comprehensions
is_divisable_by_3 = [i for i in range(1, 100) if i % 3 == 0]
print(is_divisable_by_3)
print("-------------------------------------------------------------------\n")

# Dictionary Comprehensions
hundred = {a: 'is devisable by 2' for a in range(+1, 10+1) if a % 2 == 0}
print(hundred)
print("-------------------------------------------------------------------\n")
is_divde_by_7 = {int(i/7): i for i in range(1, 100) if i % 7 == 0}
is_divde_by_7_rev = {value: key for key, value in is_divde_by_7.items()}
print((is_divde_by_7))
print((is_divde_by_7_rev))
print("-------------------------------------------------------------------\n")

# Set Comprehensions
a = {b for b in range(1, 201) if b % 5 == 0}
print((a))
print("-------------------------------------------------------------------\n")

# Generators Comprehensions
oddnum = (i for i in range(1, 100) if i % 2 == 1)
for i in oddnum:
    print(i, end=" ")
