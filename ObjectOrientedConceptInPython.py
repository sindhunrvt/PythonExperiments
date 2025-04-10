"""
Problem:
Create a class BankAccount that has the following methods:

deposit(amount): Adds the amount to the balance.

withdraw(amount): Subtracts the amount from the balance.

get_balance(): Returns the current balance.

__str__() (String method): Returns a string that shows the balance.

Extra:
Add an exception to handle withdrawals that exceed the balance.
"""
from abc import ABCMeta
from typing import AbstractSet


class InsufficientFundsError(Exception):
    pass
class InvalidAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, acc_balance):
        self.acc_balance = acc_balance
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError
        else:
            amount = int(amount)
            self.acc_balance+=amount
            print (f"Amount {amount} credited to the Account")

    def withdraw(self, amount):
        if isinstance(amount, str):
            raise InvalidAmountError("Unsupported amount Type")
        elif amount <= 0:
            raise InvalidAmountError("Invalid Amount Type")
        elif amount > self.acc_balance:
            raise InsufficientFundsError
        else:
            self.acc_balance-=amount
            print(f"Amount of {amount} withdraw")
    def get_balance(self):
        return self.acc_balance

    def __str__(self):
        return f"Balance is {self.acc_balance}"

acc1 = BankAccount(1000)
print(acc1)
try:
    acc1.withdraw(2000)
except InsufficientFundsError as e:
    print (f"Error is {e}")

try:
    acc1.withdraw('a')
except InvalidAmountError as e:
    print(f"Error is {e}")

print(acc1)
print(acc1.get_balance())
acc1.deposit(2000)
print(acc1)

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        print(f"I am in the class : {self.__class__.__name__}")

    #@abstractmethod
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        print(f"I am in the class: {self.__class__.__name__}")
        self.radius = radius

    def getradius(self):
        return self.radius
    #def area(self):
    #    return 3.14*self.radius*self.radius
    def __str__(self):
        return f"This is a Circle with radius:{self.radius}"

class Rectangle(Shape):
    def __init__(self, length, breadth):
        print(f"I am in the class: {self.__class__.__name__}")
        self.length = length
        self.breadth = breadth
    def __str__(self):
        return f"This is a Rectangle with length = {self.length} and breadth = {self.breadth}"
    def area(self):
        return self.length * self.breadth


c1 = Circle(5)
print(c1)

r1 = Rectangle(5,8)
print(r1)

shapes = [Shape(), Circle(10), Rectangle(10,20)]
for shape in shapes:
    print(shape)
    print(f"The {shape} has the area of {shape.area():.2f}")




