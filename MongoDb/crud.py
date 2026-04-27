from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["python"]

collection = db["users"]

#Insert / Create
# Singleuser = {
#     "name" : "Urooj Rehman",
#     "email" : "urooj@gmail.com",
#     "age": 29
# }

# collection.insert_one(Singleuser)

# Read
data = collection.find()

for d in data:
    print(d)

#Update
collection.update_many(
    {"name": "Urooj Rehman"},
    {"$set": {"email": "urooj123@gmail.com"}}
)

#delete
collection.delete_one({"email":"urooj123@gmail.com"})

for d in data:
    print(d)