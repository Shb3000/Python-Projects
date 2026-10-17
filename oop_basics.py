# ------------------------------------------------------------
# 1. A class is a blueprint. An object is a thing built from it.
# ------------------------------------------------------------
class Animal:
    def __init__(self, name, age):
        # __init__ runs automatically when you create a new object.
        # "self" refers to the object being created.
        self.name = name  # attribute
        self.age = age    # attribute

    def speak(self):
        # a method: a function that belongs to a class
        print(f"{self.name} makes a sound.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age}.")

    def __str__(self):
        # controls what print(object) shows
        return f"{self.name} (age {self.age})"


# ------------------------------------------------------------
# 2. Inheritance: Dog and Cat get everything Animal has,
#    and can add or change behavior.
# ------------------------------------------------------------
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # reuse Animal's __init__
        self.breed = breed

    def speak(self):  # overriding the parent method
        print(f"{self.name} says: Woof!")

    def fetch(self):  # a new method only dogs have
        print(f"{self.name} fetches the ball.")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


# ------------------------------------------------------------
# 3. Encapsulation: protect data inside the object.
#    A leading underscore means "please don't touch directly".
# ------------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self._balance += amount
        print(f"Deposited {amount}. Balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Not enough money.")
            return
        self._balance -= amount
        print(f"Withdrew {amount}. Balance: {self._balance}")

    def get_balance(self):
        return self._balance


# ------------------------------------------------------------
# Try it out
# ------------------------------------------------------------
if __name__ == "__main__":
    print("--- Objects and methods ---")
    generic = Animal("Creature", 3)
    print(generic)
    generic.speak()
    generic.birthday()

    print("\n--- Inheritance ---")
    rex = Dog("Rex", 5, "Labrador")
    tom = Cat("Tom", 2)
    print(rex, "| breed:", rex.breed)
    rex.fetch()

    print("\n--- Polymorphism (same method, different behavior) ---")
    for pet in [generic, rex, tom]:
        pet.speak()

    print("\n--- Encapsulation ---")
    account = BankAccount("Sam", 100)
    account.deposit(50)
    account.withdraw(500)  # blocked by the rule inside the class
    account.withdraw(30)
    print("Final balance:", account.get_balance())
