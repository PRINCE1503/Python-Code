# F-string & String Formatting
name="Prince"
surname="Padmani"
a="1.My name is %s %s."%(name,surname)
print(a)
print("----------------------------")
b="2.My name is {} {}."
c=b.format(name,surname)
print(c)
print("----------------------------")
d="3.My name is {1} {0}"
e=d.format(name,surname)
print(e)
print("----------------------------")
f=f"4.My name is {name} {surname}."
print(f)
