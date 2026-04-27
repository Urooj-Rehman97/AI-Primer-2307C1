#List
# print("Enter 5 numbers:")
# numbers = []
# for i in range(5):
#     numbers.append(input(f"Enter {i+1} number: "))
#
#
# print(f"Numbers: {numbers}")
#
# #List Comprehension
# #shorthand
# num = [i for i in range(5)]
# print(num)

print("\n--------------- Mini Game to identify Even or Odd Numbers --------------------------\n")
n = int(input("How many numbers you want to enter? "))
evenNumber = []
oddNumber = []
for i in range(n):
    no = int(input(f"Enter {i+1} Number:"))
    if(no%2 == 0):
        evenNumber.append(no)
    else:
      oddNumber.append(no)

print(f"Even Numbers: {evenNumber}")
print(f"Odd Numbers: {oddNumber}")