class Car:
    def __init__(self, carname, car_brand):
        self.name = carname
        self.brand = car_brand
        print("Adding a new car to garage")

c1 = Car("Scorpio", "Mahindra")
print(c1.name, c1.brand)
