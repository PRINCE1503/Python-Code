# Lembda Function
def power(a, b): return a**b


try:
    a = int(input("Enter the Number : "))
    b = int(input("Enter the power of Number : "))
    print("The value of", a, "^", b, "=", power(a, b))
except Exception as e:
    print("ENTER VALID INPUT!")
print("-------------------------------------------")
try:
    n = int(input("Which elements do you want to sort? (1st or 2nd) : "))
    c = [[13, 49], [15, 30], [3, 9], [2006, 2004]]
    c.sort(key=lambda x: x[n-1])
    print(c)
except Exception as e:
    print("ENTER VALID INPUT!")
