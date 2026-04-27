#Decision Making Statement
age = int(input("Enter Your Age? "))
if(age>18):
    print("You are elder")
else:
    print("You are too young...")

#elif
percentage = int(input("Enter Your Percentage: "))
if(percentage >=80 and percentage<=100):
    print(f"Your Percentage: {percentage} and Grade: A-One")
elif(percentage >=70 and percentage<=79):
    print(f"Your Percentage: {percentage} and Grade: A")
elif(percentage >=60 and percentage <=69):
    print(f"Your Percentage: {percentage} and Grade: B")
elif(percentage >=50 and percentage<=59):
    print(f"Your Percentage: {percentage} and Grade: C")
else:
    print(f"Your Percentage: {percentage} You're fail")
























