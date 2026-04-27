# file = open("python.txt", "w")  #write mode
# file.write("File handling in Python")
# file.close()

# file = open("python.txt", "a")  #append mode
# file.write("\nAppend new syntax")
# file.close()
#readmode
file = open("python.txt", "r")
data = file.read()
print(data)
file.close()

#shorthand
with open("python.txt","a") as file:
    file.write("\ndufferss....")