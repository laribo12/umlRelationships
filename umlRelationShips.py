from abc import ABC, abstractmethod

# 1. Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


# 2. Composition
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom")]


# 3. Aggregation
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        self.books = books


# 4. Association
class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        customer.orders.append(self)


# 5. Dependency
class Printer:
    def print_page(self, text):
        print("Printing:", text)

class ReportGenerator:
    def __init__(self, content):
        self.content = content

    def output_report(self, printer):
        printer.print_page(self.content)


# 6. Realization / Implementation
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class GCashPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ₱{amount} via GCash.")
        return True


# RUNNING THE CODE
print("--- Inheritance ---")
my_dog = Dog("Buddy")
print(my_dog.bark())

print("\n--- Composition ---")
my_house = House()
for room in my_house.rooms:
    print("Room created:", room.name)

print("\n--- Aggregation ---")
book1 = Book("The Hobbit")
book2 = Book("1984")
my_library = Library([book1, book2])
for book in my_library.books:
    print(book.title)

print("\n--- Association ---")
alice = Customer("Alice")
order1 = Order(101, alice)
print("Customer:", order1.customer.name)
print("Order ID:", alice.orders[0].order_id)

print("\n--- Dependency ---")
my_printer = Printer()
report = ReportGenerator("Q1 Academic Performance: Excellent!")
report.output_report(my_printer)

print("\n--- Realization / Implementation ---")
gateway = GCashPayment()
success = gateway.process_payment(250.75)
print("Payment Status:", success)