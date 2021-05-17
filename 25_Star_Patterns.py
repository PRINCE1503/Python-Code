# Star Patterns
try:
    a = int(input("How many rows you want to print : "))
    b = int(input(
        "Press '1' for simple star pattern OR Press '0' for reverse star pattern : "))
    c = bool(b)
    if b == 1 or b == 0:
        if c == True:

            for i in range(1, a + 1):
                for j in range(1, i + 1):
                    print('*', end=" ")
                print()
        elif c == False:
            for i in range(a, 0, -1):
                for j in range(1, i + 1):
                    print('*', end=" ")
                print()
    else:
        print("Error! You have to enter '1' or '0'")
except Exception as E:
    print("Invalid input! Please Enter a integer!")
