class Parent:
    def show(self):
        print("This is Parent Class")

class child(Parent):
     def msg(self):
         print("This is Child Class")

ch = child()
ch.show()
ch.msg()

p = Parent()
p.show()
# p.msg()

#Multilevel Inheritance
class Vehicle:
    model = None
    color = "black"

    def __init__(self, m, c):
        self.model = m
        self.color = c
    def display(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")

class Car(Vehicle):
    brand = ""
    def __init__(self,b):
        self.brand = b

class Toyota(Car):
    def details(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Brand: {self.brand}")

ty = Toyota("Abc")
ty.details()

c = Car("M123")
c.display()