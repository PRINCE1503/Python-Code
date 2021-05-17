# Built in Module
import random
a = random.randint(0, 10)
print("The random integer between 0 to 10 is :", a)
print("---------------------")
# a=random.randint(1,5)
b = random.random()*10
print("The random number between 0 to 10 is :", b)
print("---------------------")
batsman = ["SachinTendulkar", "Virat Kohli",
           "Saurav Ganguly", "Rahul Dravid", "MS Dhoni"]
print(random.choice(batsman))
