# Map Function
def number(A):
    return A


def square(a):
    return a*a


def cube(b):
    return b*b*b

try:
    u = int(input(f"How many Numbers You have to calculate there Square and Qube : "))

    N = number, square, cube
    print("[Number,Square,Cube]")

    for i in range(1, u+1):
        a = list(map(lambda x: x(i), N))
        print(a)
except Exception :
    print("INVALID INPUT! ONLY INPUT INTEGERS!")

