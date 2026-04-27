from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["python"]

collection = db["users"]

Name =input("Enter Your Name: ")
Email = input("Enter Your Email: ")
Age = int(input("Enter Your Age: "))

user = {
    "name" : Name,
    "Email": Email,
    "age": Age
}

collection.insert_one(user)
print("User Register Successfully")