# Inumerate Function
from typing import Mapping


list = ["Mangoes", "Banana", "Apple", "Grapes", "Water Melon", "Cherry"]
for index, fruits in enumerate(list):
    if index % 2 == 0:
        print(f"{index+1}. {fruits}")
