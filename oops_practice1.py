class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person('Sindhu', 38)
p1.introduce()

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__( make, model)
        self.num_doors = num_doors

    def describe(self):
        print(f"The car is a {self.model} from {self.make} with {self.num_doors} doors.")


c1 = Car("Toyota", "Corolla", 4)
c1.describe()

class BankAccount:
    def __init__(self,amount):
        self.balance = amount
        self.deposits = 0
        self.withdrawals = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Amount is greater than the balance, Withdrawal Rejected.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrawal Accepted.")
            return True

    def get_balance(self):
        print(f"Your balance is {self.balance}")

b1 = BankAccount(500)
b1.deposit(500)
print(b1.withdraw(2000))
b1.get_balance()



