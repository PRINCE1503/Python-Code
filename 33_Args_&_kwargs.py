# Args & Kwargs

def func1(Intro, *args, **kwargs):
    print(Intro)
    for items in args:
        print(items)
    print("\nThe runs of these Batsman's is : ")
    for Batsman, runs in kwargs.items():
        print(f"{Batsman} has score {runs} in ODI.")


intro = "These are India's Top 5 batsman in ODI cricket:"
Batsman = ["SachinTendulkar", "Virat Kohli",
           "Saurav Ganguly", "Rahul Dravid", "MS Dhoni"]
Runs = {"SachinTendulkar": 18426,
        "Virat Kohli": 12169,
        "Saurav Ganguly": 11221,
        "Rahul Dravid": 10768,
        "MS Dhoni": 10599}
func1(intro, *Batsman, **Runs)
