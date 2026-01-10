#property decorator
#we can use property decorator any method of the class to use method as a property
class Student:
    def __init__(self, p, c, m):
        self.p = p
        self.c = c
        self.m = m
        self.percentage = None

    @property
    def percentage(self):
         self.percentage = (self.p + self.c + self.m) / 3
    #     return self.percentage


s1 = Student(60, 60, 60)
s1.calcpercentage()
# print("Percentage:", s1.percentage)

s1.p = 70          # change physics marks
s1.calcpercentage()   # recalculate percentage
# print("Updated Percentage:", s1.percentage)
