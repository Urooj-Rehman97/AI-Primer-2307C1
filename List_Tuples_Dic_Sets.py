# List
#Mutable (List can be changed)
courses = ["R Programming", "Tableau", "AI/ML"]
count = len(courses)
print("First Course: "+courses[0])
# print("Total Number of Courses: "+str(count))
print("Total Number of Courses: ",count)
# print(f"Total Number of Courses: {count}")
courses.append("Haddop")
print(courses)
courses[0] = "ADSE_II"
print(courses)
courses.insert(1, "MERN")
print(courses)
courses.remove("MERN")
print(courses)

first = ["abc", "xyz"]
#reference
second = first
second.append("mno")
print(first)

#Tuples
#Immutable (Tuples cannot be changed)
data = (10,20,30)
print(data)
# data.append(40)
# data[0] = 40;

#Dictionary
#Hashed-based
student = {
    "name":"Abc",
    "email":"abc@gmail.com",
    "password": "abc123"
}
print(student)
print("Student Name: "+student["name"])

#sets
#unordered
#No duplicate value
a = {1,2,3,3,4}
print(a)
b = {1,3,5}

sub = a - b
print(sub)

#Union
uni = a | b
print(uni)

un = a.union(b)
print(un)

#intersection
inter = a & b
print(inter)

n = a.intersection(b)
print(n)

marks = [10,2,3,4]