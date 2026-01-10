#multilevel 
class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod    
    def stop():
        print("Car stopped")


class Toyota(Car):    # Inheriting Car
    def __init__(self, name):
        self.name = name


class fortuner(Toyota):
    def __init_(self,type):
        self.type=type        


c1 = fortuner("pertrol")

c1.start()
c1.stop()
print("Car name:", c1.type)
