#Inheritance
#When one class(parent) derives the properties and methods of another class (parent)
#single level

class car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod    
    def stop():
        print("car stop")

class toyota:
    def __init__(self,name):
        self.name=name
c1=toyota("fortuner")
print(c1.start())