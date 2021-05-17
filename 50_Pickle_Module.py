# Pickle Module
import pickle

# Creat Pickle
# Indian_Batman = ["SachinTendulkar", "Virat Kohli",
#                  "Saurav Ganguly", "Rahul Dravid", "MS Dhoni"]
# file = "E_Indian_Batsman.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(Indian_Batman, fileobj)

# Decode Pickle
file2 = "E_Indian_Batsman.pkl"
fileobj2 = open(file2, 'rb')
Indian_Batman = pickle.load(fileobj2)
print(Indian_Batman)
