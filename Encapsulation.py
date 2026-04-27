class personal:
    salary = 50000
    __saving = 10000 #private variable starts from doubleunderscore and it cannot be access outside the class

    def display(self):
        print(f"My Savings: {self.__saving}")

print(personal.salary)


#BankAccount
class BankAccount:
    __balance = 100
    def __init__(self):
        print(f"Current Balance: {self.__balance}")
    def deposit(self, dep):
        self.__balance = self.__balance + dep
        print(f"Deposit Amount: {dep}")
        print(f"Updated Balance: {self.__balance}")

    def withdraw(self, credit):
        if(self.__balance> credit):
            self.__balance = self.__balance - credit
            print(f"Withdraw Amount: {credit}")
            print(f"Updated Balance: {self.__balance}")
        else:
            print("Your Current balance is low to the amount that you credit")

Bnk = BankAccount()
# Bnk.withdraw(10000)
Bnk.deposit(int(input("Enter Amount You want to deposit: ")))
Bnk.withdraw(int(input("Enter Amount You want to credit: ")))


