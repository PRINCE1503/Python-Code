# String Slicing
mystr = "My name is Prince."
print(mystr[:])
print("Lenght of mystr is:", len(mystr))
print("-------------------------------------------------")
print(mystr[11:17])
print(mystr[11:17:2])
print(mystr[0:18:2])
print(mystr[-7:-1])
print("The reversed mystr is :", mystr[::-1])
print("-------------------------------------------------")
print("mystr is ends with Prince. :", mystr.endswith("Prince."))
print("How many 'n' is in mystr? :", mystr.count("n"))
print("'is'started in mystr at index no.:", mystr.find("is"))
print("-------------------------------------------------")
mystr2 = "he lives in Vadodara."
print("Capitilized mystr2 is :", mystr.capitalize())
print("Lowercase mystr string is:", mystr.lower())
print("Lowercase mystr2 string is:", mystr2.upper())
print("After replace 'he' in mystr2 to 'she',the mystr2 look like this:",
      mystr2.replace("he", "she"))
