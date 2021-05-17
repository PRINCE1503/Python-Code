# Dictionary & Dictionary Functions
Batsman = {"SachinTendulkar": 18426,
           "Virat Kohli": 12169,
           "Saurav Ganguly": 11221,
           "Rahul Dravid": 10768,
           "MS Dhoni": 10599}
print("The data type of Batman is :", type(Batsman))
print("Total runs in ODI cricket of SachinTendulkar is :",
      Batsman["SachinTendulkar"])
print("Total runs in ODI cricket of Virat Kohli is :", Batsman["Virat Kohli"])
print("Total runs in ODI cricket of Saurav Ganguly is :",
      Batsman["Saurav Ganguly"])
print("Total runs in ODI cricket of Rahul Dravid is :",
      Batsman["Rahul Dravid"])
print("Total runs in ODI cricket of MS Dhoni is :", Batsman["MS Dhoni"])
Batsman["Mohammad Azharuddin"] = 9378
print(Batsman)
del Batsman["Mohammad Azharuddin"]
print(Batsman)
print("-------------------------------------------------------------------------------")
Dict1 = Batsman.copy()
del Dict1["Rahul Dravid"]
print(Dict1)
print(Batsman)
print("-------------------------------------------------------------------------------")
Dict1.update({"Rahul Dravid": 10768})
print(Dict1)
print(Batsman.keys())
print("-------------------------------------------------------------------------------")
print(Batsman.items())
