#class method
#A class method is bound ti class and recieves the class as a first implicit  argument
class person:
    name="unknown"
    def changename(self,name):
        #person.name=name
        self.__class__.name="ranjeet1"
p=person()
p.changename("ranjeet")
print(p.name)
print(person.name)     