# File I\O write() & appen() Function
a = open("D_About_Virat_Kohli.txt", "a")
x = a.write("Virat kohli is a wonderfull batsman of Indian cricket Team.\n")
y = a.write("He is a Caption of India's ODI team, T-20I team and Test team.\n")
print("You have write", x+y, "charecters in file 'D_About_Virat_Kohli.txt'.")
a.close()
