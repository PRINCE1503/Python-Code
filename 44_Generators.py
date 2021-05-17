# Generators
def generator(n):
    for i in range(n):
        yield i


a = generator(3)

for i in a:
    print(i, end=" ")

print("\n--------------------")
b = generator(4)
print(b.__next__(), end=" ")
print(b.__next__(), end=" ")
print(b.__next__(), end=" ")
