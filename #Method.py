#Method
#creat a student class that take name of student and marks of three subject as arguent in 
#constructor then  create a method to print average the marks of three subject

class Student:
    def __init__(self, st_name, marks1, marks2, marks3):
        self.name = st_name
        self.m1 = marks1
        self.m2 = marks2
        self.m3 = marks3

    def average(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        return avg

s1 = Student("Ranjeet", 50, 60, 70)

print(s1.name, s1.m1, s1.m2, s1.m3)
print("Average marks:", s1.average())

    