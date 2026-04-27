# Functions in Python
#Function with Parameter
def add(x,y):
    sum = x+y
    print("Addition",sum)
    print(f"Addition: {sum}")

add(1,3)

def sub(a,b):
    return a - b

print("Subtraction",sub(10,4))

#Default Argument
def greet(name = "Urooj Rehman"):
    print("Hello "+name)

greet()
greet("Abc")

# def myfunct():
#     pass
