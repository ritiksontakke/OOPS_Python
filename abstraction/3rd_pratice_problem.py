# ============================================================
# PILLAR: Abstraction
# PROGRAM 8: Payment System
# ============================================================
#
# PROBLEM:
# Build an abstract Payment class that defines a common
# interface for different payment methods.
#
# Abstract methods:
# - pay(amount): process the payment
# - refund(amount): process a refund
#
# Implement two concrete classes:
# - CreditCard: pay prints "Paid ₹{amount} via Credit Card."
#               refund prints "Refunded ₹{amount} to Credit Card."
# - UPI: pay prints "Paid ₹{amount} via UPI."
#        refund prints "Refunded ₹{amount} via UPI."
#
# Add a non-abstract method receipt(amount) in Payment that
# prints a formatted receipt after calling pay().
#
# EXAMPLE USAGE:
#   cc = CreditCard("Visa", "1234")
#   cc.receipt(1500)
#   # Output:
#   # Paid ₹1500 via Credit Card.
#   # ---- Receipt ----
#   # Method: CreditCard
#   # Amount: ₹1500
#   # -----------------
from abc import ABC , abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass
    
    def receipt(self, amount):
        self.pay(amount)
        print("----receipt-----")
        print(f"Method: {self.__class__.__name__}")
        print(f"Amount: {amount}")

class CreaditCard(Payment):

    def __init__(self, card_type , last_digit):
        self.card_type = card_type
        self.last_digit = last_digit

    def pay(self, amount):
        print(f"paid {amount} via credit card")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to Credit Card.")

class UPI(Payment):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"paid {amount} via upi id")
    
    def refund(self, amount):
        print(f"refund {amount} via upi id")

cc = CreaditCard("Visa", "1234")
cc.receipt(1500)

print()

upi = UPI("user@upi")
upi.receipt(800)