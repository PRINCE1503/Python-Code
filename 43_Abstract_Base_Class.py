# Abstract Base Class
from abc import abstractclassmethod, ABC


class shape(ABC):
    @abstractclassmethod
    def printarea(self):
        return 0


class rectangle(shape):
    def __init__(self, lenght, breadth):
        self.lenght = lenght
        self.breadth = breadth

    def printarea(self):  # This function is must required in all calsses
        return f"The area of rectangle is {self.breadth*self.lenght}"


class square(shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def printarea(self):
        return f"The area of square is {self.lenght*self.lenght}"


class circle(shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def printarea(self):
        return f"The area of circle with value of Pie=3.14 is {22/7*self.lenght*self.lenght}\n"f"The area of circle with value of Pie=22/7 is {3.14*self.lenght*self.lenght}"


User = input(
    "Which area you want to find: a rectangle(Press R), a square(Press S) or a circle(Press C) ? : ")
User = User.lower()
if User == "r":
    a = float(input("Enter the breadth of Rectangle : "))
    b = float(input("Enter the lenght of Rectangle : "))
    rect1 = rectangle(a, b)
    print(rect1.printarea())
elif User == "s":
    c = float(input("Enter the lenght of square : "))
    sqr1 = square(c)
    print(sqr1.printarea())
elif User == "c":
    d = float(input("Enter the radius of circle : "))
    cir1 = circle(d)
    print(cir1.printarea())
else:
    print("Error! Check your input!!")
