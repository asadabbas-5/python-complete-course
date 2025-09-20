# Lesson 16: Object-Oriented Programming

"""
This lesson covers:
- Classes and objects
- Attributes and methods
- Constructors and destructors
- Instance vs class attributes
- Method types (instance, class, static)
- Encapsulation and data hiding
- Property decorators
- Basic inheritance concepts
"""

# 1. Classes and Objects Basics
print("=== Classes and Objects Basics ===")

class Person:
    """A simple Person class"""
    
    # Class attribute (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Constructor - called when creating a new instance"""
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
        print(f"Created person: {name}")
    
    def introduce(self):
        """Instance method"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        """Method that modifies instance state"""
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(f"Person 1: {person1.introduce()}")
print(f"Person 2: {person2.introduce()}")
print(f"Species: {Person.species}")

person1.have_birthday()
print(f"After birthday: {person1.introduce()}")

# 2. Attributes and Methods
print("\n=== Attributes and Methods ===")

class BankAccount:
    """A simple bank account class"""
    
    # Class attribute
    bank_name = "Python Bank"
    
    def __init__(self, account_number, initial_balance=0):
        """Initialize account"""
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def get_transaction_history(self):
        """Get transaction history"""
        return self.transaction_history.copy()
    
    def __str__(self):
        """String representation of the object"""
        return f"Account {self.account_number}: ${self.balance}"

# Using the BankAccount class
account = BankAccount("12345", 1000)
print(f"Initial: {account}")

account.deposit(500)
account.withdraw(200)
print(f"After transactions: {account}")
print(f"Transaction history: {account.get_transaction_history()}")

# 3. Instance vs Class Attributes
print("\n=== Instance vs Class Attributes ===")

class Counter:
    """Demonstrates instance vs class attributes"""
    
    # Class attribute
    total_counters = 0
    
    def __init__(self, name):
        # Instance attributes
        self.name = name
        self.count = 0
        Counter.total_counters += 1
    
    def increment(self):
        """Increment the counter"""
        self.count += 1
    
    def get_count(self):
        """Get current count"""
        return self.count
    
    @classmethod
    def get_total_counters(cls):
        """Class method to get total number of counters"""
        return cls.total_counters

# Create multiple counters
counter1 = Counter("Counter 1")
counter2 = Counter("Counter 2")
counter3 = Counter("Counter 3")

print(f"Total counters created: {Counter.get_total_counters()}")

counter1.increment()
counter1.increment()
counter2.increment()

print(f"{counter1.name}: {counter1.get_count()}")
print(f"{counter2.name}: {counter2.get_count()}")
print(f"{counter3.name}: {counter3.get_count()}")

# 4. Method Types
print("\n=== Method Types ===")

class MathUtils:
    """Demonstrates different method types"""
    
    # Class attribute
    pi = 3.14159
    
    def __init__(self, precision=2):
        """Instance method (constructor)"""
        self.precision = precision
    
    def calculate_area(self, radius):
        """Instance method - uses instance data"""
        area = self.pi * radius ** 2
        return round(area, self.precision)
    
    @classmethod
    def from_string(cls, precision_str):
        """Class method - alternative constructor"""
        precision = int(precision_str)
        return cls(precision)
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't use instance or class data"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Static method"""
        return a * b

# Using different method types
math1 = MathUtils(3)
print(f"Area with precision 3: {math1.calculate_area(5)}")

math2 = MathUtils.from_string("4")
print(f"Area with precision 4: {math2.calculate_area(5)}")

# Static methods can be called on class or instance
print(f"Add (class): {MathUtils.add(5, 3)}")
print(f"Add (instance): {math1.add(5, 3)}")
print(f"Multiply: {MathUtils.multiply(4, 6)}")

# 5. Encapsulation and Data Hiding
print("\n=== Encapsulation and Data Hiding ===")

class Student:
    """Demonstrates encapsulation"""
    
    def __init__(self, name, student_id):
        # Public attributes
        self.name = name
        self.student_id = student_id
        
        # Private attributes (convention: single underscore)
        self._grades = []
        
        # Protected attributes (convention: double underscore)
        self.__ssn = None
    
    def add_grade(self, grade):
        """Public method to add grade"""
        if 0 <= grade <= 100:
            self._grades.append(grade)
            return True
        return False
    
    def get_gpa(self):
        """Public method to get GPA"""
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)
    
    def get_grades(self):
        """Public method to get grades (read-only)"""
        return self._grades.copy()
    
    def set_ssn(self, ssn):
        """Public method to set SSN"""
        if len(ssn) == 9 and ssn.isdigit():
            self.__ssn = ssn
            return True
        return False
    
    def get_ssn(self):
        """Public method to get masked SSN"""
        if self.__ssn:
            return f"***-**-{self.__ssn[-4:]}"
        return "Not set"

# Using encapsulation
student = Student("Alice", "12345")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)

print(f"Student: {student.name}")
print(f"GPA: {student.get_gpa():.2f}")
print(f"Grades: {student.get_grades()}")

student.set_ssn("123456789")
print(f"SSN: {student.get_ssn()}")

# 6. Property Decorators
print("\n=== Property Decorators ===")

class Rectangle:
    """Demonstrates property decorators"""
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        """Get width"""
        return self._width
    
    @width.setter
    def width(self, value):
        """Set width with validation"""
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be positive")
    
    @property
    def height(self):
        """Get height"""
        return self._height
    
    @height.setter
    def height(self, value):
        """Set height with validation"""
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be positive")
    
    @property
    def area(self):
        """Calculate area (read-only property)"""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Calculate perimeter (read-only property)"""
        return 2 * (self._width + self._height)

# Using properties
rect = Rectangle(5, 10)
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")

# Using setters
rect.width = 8
rect.height = 12
print(f"New area: {rect.area}")

# 7. Basic Inheritance
print("\n=== Basic Inheritance ===")

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Base method - can be overridden"""
        return "Some generic animal sound"
    
    def move(self):
        """Base method"""
        return f"{self.name} moves"
    
    def __str__(self):
        return f"{self.name} the {self.species}"

class Dog(Animal):
    """Dog class inherits from Animal"""
    
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        """Override parent method"""
        return "Woof!"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """Cat class inherits from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        """Override parent method"""
        return "Meow!"
    
    def climb(self):
        """Cat-specific method"""
        return f"{self.name} climbs the tree"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(f"Dog: {dog}")
print(f"Dog sound: {dog.make_sound()}")
print(f"Dog action: {dog.fetch()}")

print(f"Cat: {cat}")
print(f"Cat sound: {cat.make_sound()}")
print(f"Cat action: {cat.climb()}")

# 8. Method Overriding and super()
print("\n=== Method Overriding and super() ===")

class Vehicle:
    """Base vehicle class"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def start(self):
        """Start the vehicle"""
        return f"{self.year} {self.make} {self.model} started"
    
    def accelerate(self, amount):
        """Accelerate the vehicle"""
        self.speed += amount
        return f"Speed increased to {self.speed} mph"
    
    def brake(self, amount):
        """Brake the vehicle"""
        self.speed = max(0, self.speed - amount)
        return f"Speed decreased to {self.speed} mph"

class Car(Vehicle):
    """Car class inherits from Vehicle"""
    
    def __init__(self, make, model, year, doors):
        # Call parent constructor
        super().__init__(make, model, year)
        self.doors = doors
    
    def start(self):
        """Override parent method"""
        # Call parent method and extend it
        parent_result = super().start()
        return f"{parent_result} - Car with {self.doors} doors"

class Motorcycle(Vehicle):
    """Motorcycle class inherits from Vehicle"""
    
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def start(self):
        """Override parent method"""
        parent_result = super().start()
        return f"{parent_result} - Motorcycle with {self.engine_size}cc engine"
    
    def wheelie(self):
        """Motorcycle-specific method"""
        return f"{self.year} {self.make} {self.model} does a wheelie!"

# Using inheritance with method overriding
car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Honda", "CBR600", 2023, 600)

print(f"Car: {car.start()}")
print(f"Car acceleration: {car.accelerate(30)}")

print(f"Motorcycle: {motorcycle.start()}")
print(f"Motorcycle action: {motorcycle.wheelie()}")

# 9. Multiple Inheritance
print("\n=== Multiple Inheritance ===")

class Flyable:
    """Mixin class for flying capability"""
    
    def fly(self):
        return f"{self.name} is flying"
    
    def land(self):
        return f"{self.name} has landed"

class Swimmable:
    """Mixin class for swimming capability"""
    
    def swim(self):
        return f"{self.name} is swimming"
    
    def dive(self):
        return f"{self.name} is diving"

class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from Animal and mixins"""
    
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def make_sound(self):
        return "Quack!"

# Using multiple inheritance
duck = Duck("Donald")
print(f"Duck: {duck}")
print(f"Duck sound: {duck.make_sound()}")
print(f"Duck action 1: {duck.fly()}")
print(f"Duck action 2: {duck.swim()}")

# 10. Abstract Classes
print("\n=== Abstract Classes ===")

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def describe(self):
        """Concrete method"""
        return f"This is a {self.name}"

class Circle(Shape):
    """Circle class implements Shape"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Implement abstract method"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """Implement abstract method"""
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    """Rectangle class implements Shape"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Implement abstract method"""
        return self.width * self.height
    
    def perimeter(self):
        """Implement abstract method"""
        return 2 * (self.width + self.height)

# Using abstract classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle: {circle.describe()}")
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")

print(f"Rectangle: {rectangle.describe()}")
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Library Management System
class Book:
    """Book class for library system"""
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower = None
    
    def borrow(self, borrower_name):
        """Borrow the book"""
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrower = borrower_name
            return True
        return False
    
    def return_book(self):
        """Return the book"""
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrower = None
            return True
        return False
    
    def __str__(self):
        status = f"Borrowed by {self.borrower}" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    """Library class to manage books"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """Add book to library"""
        self.books.append(book)
    
    def find_book(self, title):
        """Find book by title"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def borrow_book(self, title, borrower):
        """Borrow a book"""
        book = self.find_book(title)
        if book and book.borrow(borrower):
            return True
        return False
    
    def return_book(self, title):
        """Return a book"""
        book = self.find_book(title)
        if book:
            return book.return_book()
        return False
    
    def list_available_books(self):
        """List all available books"""
        return [book for book in self.books if not book.is_borrowed]

# Test library system
library = Library("City Library")

# Add books
library.add_book(Book("Python Programming", "John Doe", "123456789"))
library.add_book(Book("Data Structures", "Jane Smith", "987654321"))
library.add_book(Book("Algorithms", "Bob Johnson", "456789123"))

# Borrow books
library.borrow_book("Python Programming", "Alice")
library.borrow_book("Data Structures", "Bob")

# List books
print("All books:")
for book in library.books:
    print(f"  {book}")

print("\nAvailable books:")
for book in library.list_available_books():
    print(f"  {book}")

# Example 2: Employee Management System
class Employee:
    """Base employee class"""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def calculate_pay(self):
        """Calculate monthly pay"""
        return self.salary
    
    def get_info(self):
        """Get employee information"""
        return f"ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    """Manager class inherits from Employee"""
    
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self.bonus = bonus
    
    def calculate_pay(self):
        """Override to include bonus"""
        return self.salary + self.bonus
    
    def get_info(self):
        """Override to include bonus info"""
        base_info = super().get_info()
        return f"{base_info}, Bonus: ${self.bonus}"

class Developer(Employee):
    """Developer class inherits from Employee"""
    
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language
    
    def get_info(self):
        """Override to include programming language"""
        base_info = super().get_info()
        return f"{base_info}, Language: {self.programming_language}"

# Test employee system
employees = [
    Employee("Alice", "E001", 50000),
    Manager("Bob", "E002", 70000, 10000),
    Developer("Charlie", "E003", 60000, "Python")
]

print("\nEmployee Information:")
for emp in employees:
    print(f"  {emp.get_info()}")
    print(f"  Monthly Pay: ${emp.calculate_pay()}")

# 12. Best Practices
print("\n=== Best Practices ===")

# Best Practice 1: Use descriptive class and method names
class UserAccount:  # Good
    def calculate_monthly_interest(self):  # Good
        pass

# Best Practice 2: Keep classes focused (Single Responsibility Principle)
class EmailSender:  # Good - focused on sending emails
    pass

class UserValidator:  # Good - focused on validation
    pass

# Best Practice 3: Use properties for computed attributes
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

# Best Practice 4: Use composition over inheritance when appropriate
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()

# Exercises:
"""
1. Create a class for a bank account with deposit, withdraw, and balance methods
2. Create a class hierarchy for different types of vehicles (car, motorcycle, truck)
3. Create a class for a shopping cart with add, remove, and calculate total methods
4. Create a class for a student with methods to add grades and calculate GPA
5. Create a class for a simple calculator with basic operations
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Bank account class
print("Exercise 1: Bank Account Class")
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def get_transactions(self):
        return self.transactions.copy()

account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")
print(f"Transactions: {account.get_transactions()}")

# 2. Vehicle hierarchy
print("\nExercise 2: Vehicle Hierarchy")
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def start(self):
        return f"{self.year} {self.make} {self.model} started"
    
    def accelerate(self, amount):
        self.speed += amount
        return f"Speed: {self.speed} mph"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def honk(self):
        return "Beep beep!"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def wheelie(self):
        return "Doing a wheelie!"

car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Honda", "CBR", 2023, 600)

print(f"Car: {car.start()}")
print(f"Car honk: {car.honk()}")
print(f"Motorcycle: {motorcycle.start()}")
print(f"Motorcycle wheelie: {motorcycle.wheelie()}")

# 3. Shopping cart class
print("\nExercise 3: Shopping Cart Class")
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] -= quantity
            if self.items[item]['quantity'] <= 0:
                del self.items[item]
    
    def calculate_total(self):
        total = 0
        for item, details in self.items.items():
            total += details['price'] * details['quantity']
        return total
    
    def get_items(self):
        return self.items.copy()

cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.add_item("Banana", 0.75, 5)
cart.add_item("Orange", 2.00, 2)

print(f"Cart total: ${cart.calculate_total():.2f}")
print(f"Items: {cart.get_items()}")

# 4. Student class
print("\nExercise 4: Student Class")
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        gpa = self.calculate_gpa()
        if gpa >= 90:
            return "A"
        elif gpa >= 80:
            return "B"
        elif gpa >= 70:
            return "C"
        elif gpa >= 60:
            return "D"
        else:
            return "F"

student = Student("Alice", "12345")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.add_grade(88)

print(f"Student: {student.name}")
print(f"GPA: {student.calculate_gpa():.2f}")
print(f"Letter Grade: {student.get_letter_grade()}")

# 5. Calculator class
print("\nExercise 5: Calculator Class")
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        return self.history.copy()
    
    def clear_history(self):
        self.history.clear()

calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"History: {calc.get_history()}")

print("\n🎉 Congratulations! You've completed Lesson 16!")
print("Next: Lesson 17 - Advanced OOP")
