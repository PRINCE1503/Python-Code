# My Dictionary
print("This is a dictionary about Indian Batsman's average in ODI cricket")
Batsman = {"Sachin Tendulkar": 44.83,
           "Virat Kohli": 59.07,
           "Saurav Ganguly": 40.95,
           "Rahul Dravid": 39.15,
           "MS Dhoni": 50.23,
           "Mohammad Azharuddin": 36.92,
           "Rohit Sharma": 48.96,
           "Yuvraj Singh": 36.47,
           "Virendra Sehwag": 35.37,
           "Shikhar Dhawan": 45.28}
avg = input(str("Enter the name of Batsman: "))
print("The average of", avg, "is", Batsman[avg])
