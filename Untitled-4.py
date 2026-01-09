#class/instance attribute
#example
# self.name is a instance attribute because it is unique attribute
#  as respect to object
#class attribute are common to all
#obj att> class att

class student:
    college_name="dyp"
    def __init__(self,st_name,st_roll_no):
        self.name=st_name
        self.roll_no=st_roll_no
        print("adding students")
s1=student("ranjeet",36)
print(s1.name,s1.roll_no)   
print(s1.college_name)     