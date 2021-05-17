# Single Inharitance
class Batsman:
    def __init__(self, Name, Runs, Best, Average):
        self.Name = Name
        self.Runs = Runs
        self.Average = Average
        self.Best = Best

    def Player_Details(self):
        return f"\nThe name of Batsman is {self.Name}.He scores {self.Runs} Runs with average of {self.Average} in ODI cricket.His best score is {self.Best} Runs."


Sachin = Batsman("Sachin Tendulkar", "18426", "200*", "44.8")
Virat = Batsman("Virat Kohali", "12169", "183", "59.07")
Saurav = Batsman("Saurav Ganguly", "11221", "183", "40.95")
Rahul = Batsman("Rahul Dravid", "10768", "153", "39.15")
Ms = Batsman("MS Dhoni", "10599", "183*", "50.23")
print(Sachin.Player_Details())
print(Virat.Player_Details())
print(Saurav.Player_Details())
print(Rahul.Player_Details())
print(Ms.Player_Details())

print("-----------------------------------------------------------------------------------------------------------------------------\n""-----------------------------------------------------------------------------------------------------------------------------\n""-----------------------------------------------------------------------------------------------------------------------------")


class Batsman_Fifties(Batsman):
    def __init__(self, Name, Runs, Best, Average, sr):
        super().__init__(Name, Runs, Best, Average)
        self.sr = sr

    def printinfo(self):
        return f"\nThe name of Batsman is {self.Name}.He scores {self.Runs} Runs with average of {self.Average} and Strike Rate of{self.sr} in ODI cricket.His best score is {self.Best} Runs."


Sachin = Batsman_Fifties("Sachin Tendulkar", "18426", "200*", "44.8", "86.23")
Virat = Batsman_Fifties("Virat Kohali", "12169", "183", "59.07", "93.17")
Saurav = Batsman_Fifties("Saurav Ganguly", "11221", "183", "40.95", "73.65")
Rahul = Batsman_Fifties("Rahul Dravid", "10768", "153", "39.15", "71.18")
Ms = Batsman_Fifties("MS Dhoni", "10599", "183*", "50.23", "87.13")
print(Sachin.printinfo())
print(Virat.printinfo())
print(Saurav.printinfo())
print(Rahul.printinfo())
print(Ms.printinfo())
