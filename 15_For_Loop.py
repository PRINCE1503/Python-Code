# For Loop
list1 = ["Sachin_Tendulkar",
         "Virat_Kohli",
         "Saurav_Ganguly",
         "Rahul_Dravid",
         "MS_Dhoni"]
for items in list1:
    print("Player Name:", items)
print("\n-------------------------------------------------------------------------")
list2 = [["SachinTendulkar", 18426],
         ["Virat Kohli", 12169],
         ["Saurav Ganguly", 11221],
         ["Rahul Dravid", 10768],
         ["MS Dhoni", 10599]]

for items, runs in list2:
    print(items, "-", runs, "Runs")
