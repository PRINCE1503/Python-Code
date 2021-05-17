# Filter Functiom
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_greater_than_5(a):
    return a > 5


grtn5 = list(filter(is_greater_than_5, l1))
print("These numbers are graeter than 5 : ")
print(grtn5)