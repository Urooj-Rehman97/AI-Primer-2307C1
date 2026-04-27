#Polymorphism
#Method Overloading

# def len():
#     print(f"Length: {len}")
#
# def len(n):
#     print(f"Length: {n}")
#
# len(12)
# len(10)

class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.sound()

#Method Overriding

class Parent:
    def show(self):
        print("Show Parent....")
class Child(Parent):
    def show(self):
        print("Show Child....")

c = Child()
c.show()