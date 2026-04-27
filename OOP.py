#OOP

class student:
     id = 121
     name = "Abc"
     email = "abc@gmail.com"
     def details(self):
         print(f"Student Id: {self.id}")
         print(f"Student Name: {self.name}")
         print(f"Student Email: {self.email}")
# In other languages
# student s1 =new student()

# In python
s1 = student()
s1.details()

#constructor
class employee:
    id = None
    name = None
    email = None

    def __init__(self, id,name ,email):
        self.id = id
        self.name = name
        self.email =email
    def details(self):
        print(f"Student Id: {self.id}")
        print(f"Student Name: {self.name}")
        print(f"Student Email: {self.email}")





id = input("Enter your Emp Id: ")
name = input("Enter your Name: ")
email = input("Enter your Email: ")
e1 = employee(id, name, email)
e1.details()

#Instance Variable Vs Class Variable
class std:
    school = "Abc School"  #class variable
    def __init__(self,name):  #name is instance variable
        self.name = std.school