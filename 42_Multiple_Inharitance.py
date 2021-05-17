# Multiple Inharitance
class Batsman:
    def __init__(self, Name, Runs):
        self.Name = Name
        self.Runs = Runs

    def Player_Details(self):
        return f"\nThe name of Batsman is {self.Name}.He scores {self.Runs} Runs."


class Bat_Best_and_Avg(Batsman):
    def __init__(self, Name, Runs, Best, Avg):
        super().__init__(Name, Runs)
        self.Best = Best
        self.Avg = Avg

    def Player_Details_update(self):
        return f"\nThe name of Batsman is {self.Name}.He scores {self.Runs} Runs with average of {self.Avg}.His highest Score is {self.Best}"


class Full_Batsman_Details(Bat_Best_and_Avg, Batsman):

    def __init__(self, Name, Runs, Best, Avg, sr):
        super().__init__(Name, Runs, Best, Avg)
        self.sr = sr

    def latestimfo(self):
        return f"\nThe name of Batsman is {self.Name}.He scores {self.Runs} Runs with average of {self.Avg} and Strike Rate of{self.sr} in ODI cricket.His best score is {self.Best} Runs."


Sachin = Full_Batsman_Details(
    "Sachin Tendulkar", "18426", "200*", "44.8", "86.23")
Virat = Full_Batsman_Details("Virat Kohali", "12169", "183", "59.07", "93.17")
Saurav = Full_Batsman_Details(
    "Saurav Ganguly", "11221", "183", "40.95", "73.65")
Rahul = Full_Batsman_Details("Rahul Dravid", "10768", "153", "39.15", "71.18")
Ms = Full_Batsman_Details("MS Dhoni", "10599", "183*", "50.23", "87.13")
print(Sachin.latestimfo())
print(Virat.latestimfo())
print(Saurav.latestimfo())
print(Rahul.latestimfo())
print(Ms.latestimfo())
