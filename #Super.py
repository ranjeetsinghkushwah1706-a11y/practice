#Super
# super method is access rthe method of the parent class


class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class toyota(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

car1=toyota("fortuner","petrol")

print(car1.type)