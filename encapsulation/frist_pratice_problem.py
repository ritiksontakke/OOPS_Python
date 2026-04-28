# PILLAR: Encapsulation # PROGRAM 1: 
# Bank Account # ============================================================ # #
#  PROBLEM: # Create a BankAccount class that protects its balance.
#  # - The balance should NOT be directly accessible from outside.
#  # - Users must use deposit(), withdraw(), and get_balance() methods.
#  # # RULES: # - balance starts at 0 (or a given amount)
#  # - deposit amount must be positive
#  # - withdraw must not exceed current balance
#  # - get_balance() returns the current balance
#  # EXAMPLE USAGE: # acc = BankAccount("Alice", 1000) 
# # acc.deposit(500) # balance = 1500 # acc.withdraw(200)
#  # balance = 1300 # print(acc.get_balance()) # 1300

class BankAccount:
    def __init__(self , owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount} . New Balance : {self.__balance}")

    def withdraw(self, amount):
        if amount <=0:
            print("Withdraw Amount Must Be Positive")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdraw {amount} . New Balance {self.__balance}")
    def get_balance(self):
        return self.__balance

acc = BankAccount("ritik" , 100)
acc.deposit(500)
acc.withdraw(50)
print(acc.get_balance())