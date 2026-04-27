#Exception Handling
try:
    print(10/0)
except:
    print("Invalid Operation")
# print(10/0)
print("abcdkgh")

#else
try:
    name = int("Abc")
except:
    print("Type Conversion Error")
else:
    print(f"Name: {name}")
finally:
    print("finally Block invokes...")


#Exception Handling Task
try:
    num1 = int(input("Enter 1st Value: "))
    num2 = int(input("Enter 2nd Value: "))
    division = num1/num2
except:
    print("Denominator should not be zero")
else:
    print(f"Division of given numbers: {division}")
finally:
    print("The End")