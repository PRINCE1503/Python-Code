# Class ,Constructors, Classmethods
class Student():
    def __init__(self, name, std, group):
        self.name = name
        self.std = std
        self.group = group

    def Studentimfo(self):
        return f"\nThe name of student is {self.name}. {self.name} is studying in Std {self.std} {self.group}."

    @classmethod
    def split_via_dash(cls, x):
        a = x.split("-")
        return cls(a[0], a[1], a[2])


Prince = Student("Prince", "11 Science", "Biology")
Meet = Student("Meet", "11 Science", "Maths")
Karan = Student.split_via_dash("Karan-8-A")

print(Meet.Studentimfo())
print(Prince.Studentimfo())
print(Karan.Studentimfo())
print()
