#abstraction
#Hiding the implementation details of class and only showing the essential feature to the user
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clt=False
    def carstart(self):
        self.acc=True
        self.clt=True
        print("car started")
c1=car()
c1.carstart()            