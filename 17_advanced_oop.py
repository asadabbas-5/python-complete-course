# Lesson 17: Advanced OOP

"""
This lesson covers:
- Polymorphism and method overriding
- Encapsulation with private attributes
- Abstract classes and interfaces
- Composition vs inheritance
- Method resolution order (MRO)
- Special methods (__str__, __repr__, etc.)
- Class decorators and metaclasses basics
- Design patterns in OOP
"""

# 1. Polymorphism and Method Overriding
print("=== Polymorphism and Method Overriding ===")

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """Base method - should be overridden"""
        return "Some generic animal sound"
    
    def move(self):
        """Base method"""
        return f"{self.name} moves"

class Dog(Animal):
    """Dog class"""
    
    def make_sound(self):
        """Override parent method"""
        return "Woof!"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """Cat class"""
    
    def make_sound(self):
        """Override parent method"""
        return "Meow!"
    
    def climb(self):
        """Cat-specific method"""
        return f"{self.name} climbs the tree"

class Bird(Animal):
    """Bird class"""
    
    def make_sound(self):
        """Override parent method"""
        return "Tweet!"
    
    def fly(self):
        """Bird-specific method"""
        return f"{self.name} flies away"

# Polymorphism in action
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety"),
    Animal("Generic")
]

print("Animal sounds:")
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")

# 2. Encapsulation with Private Attributes
print("\n=== Encapsulation with Private Attributes ===")

class BankAccount:
    """Bank account with proper encapsulation"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute
        self.__transaction_history = []   # Private attribute
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_balance(self):
        """Public method to get balance"""
        return self.__balance
    
    def get_transaction_history(self):
        """Public method to get transaction history"""
        return self.__transaction_history.copy()
    
    def __validate_transaction(self, amount):
        """Private method for validation"""
        return amount > 0

# Test encapsulation
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)

print(f"Balance: ${account.get_balance()}")
print(f"Transaction history: {account.get_transaction_history()}")

# Try to access private attributes (not recommended)
# print(account.__balance)  # This would cause an AttributeError

# 3. Abstract Classes and Interfaces
print("\n=== Abstract Classes and Interfaces ===")

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method - must be implemented"""
        pass
    
    def describe(self):
        """Concrete method"""
        return f"This is a {self.name}"

class Circle(Shape):
    """Circle implementation"""
    
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
    """Rectangle implementation"""
    
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
shapes = [
    Circle(5),
    Rectangle(4, 6)
]

for shape in shapes:
    print(f"{shape.describe()}")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

# 4. Composition vs Inheritance
print("\n=== Composition vs Inheritance ===")

# Inheritance approach
class Engine:
    """Engine class"""
    
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return "Engine started"
    
    def stop(self):
        self.is_running = False
        return "Engine stopped"

class CarWithInheritance:
    """Car using inheritance"""
    
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"

# Composition approach
class CarWithComposition:
    """Car using composition"""
    
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition - has-a relationship
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"

# Test both approaches
car1 = CarWithInheritance("Toyota", "Camry", 200)
car2 = CarWithComposition("Honda", "Civic", Engine(180))

print(f"Inheritance: {car1.start()}")
print(f"Composition: {car2.start()}")

# 5. Method Resolution Order (MRO)
print("\n=== Method Resolution Order (MRO) ===")

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    def method(self):
        return "D"

# Check MRO
print(f"D MRO: {D.__mro__}")
print(f"D method: {D().method()}")

# Diamond inheritance problem
class Base:
    def method(self):
        return "Base"

class Left(Base):
    def method(self):
        return "Left"

class Right(Base):
    def method(self):
        return "Right"

class Bottom(Left, Right):
    pass

print(f"Bottom MRO: {Bottom.__mro__}")
print(f"Bottom method: {Bottom().method()}")

# 6. Special Methods (Magic Methods)
print("\n=== Special Methods (Magic Methods) ===")

class Point:
    """Point class with special methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __add__(self, other):
        """Addition operator"""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __len__(self):
        """Length (distance from origin)"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __bool__(self):
        """Boolean conversion"""
        return self.x != 0 or self.y != 0

# Test special methods
p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Point 1 == Point 3: {p1 == p3}")
print(f"Point 1 + Point 2: {p1 + p2}")
print(f"Length of Point 1: {len(p1)}")
print(f"Boolean of Point 1: {bool(p1)}")

# 7. Class Decorators
print("\n=== Class Decorators ===")

def singleton(cls):
    """Singleton decorator"""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    """Singleton database connection"""
    
    def __init__(self):
        self.connection_id = id(self)
        print(f"Database connection created: {self.connection_id}")
    
    def query(self, sql):
        return f"Executing: {sql}"

# Test singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")
print(f"Connection ID: {db1.connection_id}")

# Property decorator for classes
def property_class(cls):
    """Class decorator to add properties"""
    for name, method in cls.__dict__.items():
        if hasattr(method, '__get__'):
            setattr(cls, name, property(method))
    return cls

# 8. Design Patterns
print("\n=== Design Patterns ===")

# Factory Pattern
class AnimalFactory:
    """Factory for creating animals"""
    
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        elif animal_type == "bird":
            return Bird(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Test factory pattern
factory = AnimalFactory()
dog = factory.create_animal("dog", "Rex")
cat = factory.create_animal("cat", "Fluffy")

print(f"Factory created: {dog.name} - {dog.make_sound()}")
print(f"Factory created: {cat.name} - {cat.make_sound()}")

# Observer Pattern
class Subject:
    """Subject in observer pattern"""
    
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer:
    """Observer in observer pattern"""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, event):
        print(f"{self.name} received event: {event}")

# Test observer pattern
subject = Subject()
observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Something happened!")

# Strategy Pattern
class PaymentStrategy:
    """Base payment strategy"""
    
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentStrategy):
    """Credit card payment strategy"""
    
    def pay(self, amount):
        return f"Paid ${amount} with credit card"

class PayPalPayment(PaymentStrategy):
    """PayPal payment strategy"""
    
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class PaymentProcessor:
    """Payment processor using strategy pattern"""
    
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def process_payment(self, amount):
        return self.payment_strategy.pay(amount)

# Test strategy pattern
credit_card = CreditCardPayment()
paypal = PayPalPayment()

processor1 = PaymentProcessor(credit_card)
processor2 = PaymentProcessor(paypal)

print(f"Credit card: {processor1.process_payment(100)}")
print(f"PayPal: {processor2.process_payment(100)}")

# 9. Advanced Inheritance Concepts
print("\n=== Advanced Inheritance Concepts ===")

class Vehicle:
    """Base vehicle class"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def start(self):
        return f"{self.year} {self.make} {self.model} started"
    
    def accelerate(self, amount):
        self.speed += amount
        return f"Speed increased to {self.speed} mph"

class ElectricVehicle(Vehicle):
    """Electric vehicle mixin"""
    
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery charged to {self.battery_level}%"
    
    def get_range(self):
        return f"Range: {self.battery_level * self.battery_capacity / 100} miles"

class HybridVehicle(Vehicle):
    """Hybrid vehicle mixin"""
    
    def __init__(self, make, model, year, fuel_capacity, battery_capacity):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
        self.battery_capacity = battery_capacity
        self.fuel_level = 100
        self.battery_level = 100
    
    def refuel(self, amount):
        self.fuel_level = min(100, self.fuel_level + amount)
        return f"Fuel tank filled to {self.fuel_level}%"
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery charged to {self.battery_level}%"

class ElectricCar(ElectricVehicle):
    """Electric car"""
    
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year, battery_capacity)
        self.doors = 4
    
    def start(self):
        return f"Electric {super().start()} - Silent operation"

class HybridCar(HybridVehicle):
    """Hybrid car"""
    
    def __init__(self, make, model, year, fuel_capacity, battery_capacity):
        super().__init__(make, model, year, fuel_capacity, battery_capacity)
        self.doors = 4
    
    def start(self):
        return f"Hybrid {super().start()} - Efficient operation"

# Test advanced inheritance
electric_car = ElectricCar("Tesla", "Model 3", 2023, 75)
hybrid_car = HybridCar("Toyota", "Prius", 2023, 45, 1.3)

print(f"Electric car: {electric_car.start()}")
print(f"Electric car range: {electric_car.get_range()}")
print(f"Electric car charge: {electric_car.charge(20)}")

print(f"Hybrid car: {hybrid_car.start()}")
print(f"Hybrid car refuel: {hybrid_car.refuel(30)}")
print(f"Hybrid car charge: {hybrid_car.charge(15)}")

# 10. Metaclasses Basics
print("\n=== Metaclasses Basics ===")

class SingletonMeta(type):
    """Metaclass for singleton pattern"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    """Logger using singleton metaclass"""
    
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)
        print(f"Log: {message}")
    
    def get_logs(self):
        return self.logs.copy()

# Test metaclass
logger1 = Logger()
logger2 = Logger()

print(f"Same instance: {logger1 is logger2}")
logger1.log("First log")
logger2.log("Second log")
print(f"All logs: {logger1.get_logs()}")

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Game Character System
class Character:
    """Base character class"""
    
    def __init__(self, name, health=100, attack=10):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        return f"{self.name} took {damage} damage. Health: {self.health}"
    
    def attack_target(self, target):
        damage = self.attack
        return target.take_damage(damage)
    
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        return f"{self.name} healed {amount}. Health: {self.health}"
    
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    """Warrior class"""
    
    def __init__(self, name):
        super().__init__(name, health=120, attack=15)
        self.armor = 5
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.armor)
        return super().take_damage(actual_damage)
    
    def charge_attack(self, target):
        damage = self.attack * 2
        return f"{self.name} charges! {target.take_damage(damage)}"

class Mage(Character):
    """Mage class"""
    
    def __init__(self, name):
        super().__init__(name, health=80, attack=20)
        self.mana = 100
    
    def cast_fireball(self, target):
        if self.mana >= 30:
            self.mana -= 30
            damage = self.attack * 1.5
            return f"{self.name} casts fireball! {target.take_damage(int(damage))}"
        return f"{self.name} doesn't have enough mana!"

# Test game system
warrior = Warrior("Conan")
mage = Mage("Gandalf")

print(f"Warrior: {warrior.name}, Health: {warrior.health}")
print(f"Mage: {mage.name}, Health: {mage.health}")

print(f"Warrior attacks mage: {warrior.attack_target(mage)}")
print(f"Mage casts fireball: {mage.cast_fireball(warrior)}")
print(f"Warrior charges: {warrior.charge_attack(mage)}")

# Example 2: Employee Management System
class Employee:
    """Base employee class"""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = None
    
    def calculate_pay(self):
        return self.salary
    
    def get_info(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    """Manager class"""
    
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self.bonus = bonus
        self.team = []
    
    def calculate_pay(self):
        return self.salary + self.bonus
    
    def add_team_member(self, employee):
        self.team.append(employee)
        employee.department = self.name
    
    def get_team_size(self):
        return len(self.team)

class Developer(Employee):
    """Developer class"""
    
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language
        self.projects = []
    
    def add_project(self, project):
        self.projects.append(project)
    
    def get_project_count(self):
        return len(self.projects)

# Test employee system
manager = Manager("Alice", "M001", 80000, 15000)
dev1 = Developer("Bob", "D001", 70000, "Python")
dev2 = Developer("Charlie", "D002", 75000, "Java")

manager.add_team_member(dev1)
manager.add_team_member(dev2)

dev1.add_project("Web App")
dev1.add_project("API Service")

print(f"Manager: {manager.get_info()}")
print(f"Manager pay: ${manager.calculate_pay()}")
print(f"Team size: {manager.get_team_size()}")

print(f"Developer: {dev1.get_info()}")
print(f"Projects: {dev1.get_project_count()}")

# 12. Best Practices
print("\n=== Best Practices ===")

# Best Practice 1: Use composition over inheritance when possible
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition
    
    def start(self):
        return self.engine.start()

# Best Practice 2: Keep inheritance hierarchies shallow
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

# Best Practice 3: Use abstract base classes for interfaces
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Best Practice 4: Use properties for computed attributes
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14159 * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self.radius

# Best Practice 5: Use special methods appropriately
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Exercises:
"""
1. Create a class hierarchy for different types of media (book, movie, music)
2. Implement a simple banking system with different account types
3. Create a shape hierarchy with area and perimeter calculations
4. Implement a simple game with different character types
5. Create a vehicle hierarchy with different propulsion methods
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Media hierarchy
print("Exercise 1: Media Hierarchy")
class Media:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    
    def get_info(self):
        return f"{self.title} ({self.year})"

class Book(Media):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return f"Book: {super().get_info()} by {self.author}, {self.pages} pages"

class Movie(Media):
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self.director = director
        self.duration = duration
    
    def get_info(self):
        return f"Movie: {super().get_info()} by {self.director}, {self.duration} min"

class Music(Media):
    def __init__(self, title, year, artist, genre):
        super().__init__(title, year)
        self.artist = artist
        self.genre = genre
    
    def get_info(self):
        return f"Music: {super().get_info()} by {self.artist}, {self.genre}"

media_items = [
    Book("Python Programming", 2023, "John Doe", 400),
    Movie("Inception", 2010, "Christopher Nolan", 148),
    Music("Bohemian Rhapsody", 1975, "Queen", "Rock")
]

for item in media_items:
    print(item.get_info())

# 2. Banking system
print("\nExercise 2: Banking System")
class Account:
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

class SavingsAccount(Account):
    def __init__(self, account_number, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest: +${interest:.2f}")
        return interest

class CheckingAccount(Account):
    def __init__(self, account_number, initial_balance=0, overdraft_limit=100):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False

savings = SavingsAccount("S001", 1000)
checking = CheckingAccount("C001", 500)

savings.deposit(200)
savings.add_interest()
checking.withdraw(600)  # Overdraft

print(f"Savings balance: ${savings.get_balance():.2f}")
print(f"Checking balance: ${checking.get_balance()}")

# 3. Shape hierarchy
print("\nExercise 3: Shape Hierarchy")
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError
    
    def perimeter(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base + self.side1 + self.side2

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5, 5)
]

for shape in shapes:
    print(f"{shape.name}: Area={shape.area():.2f}, Perimeter={shape.perimeter():.2f}")

# 4. Game character system
print("\nExercise 4: Game Character System")
class GameCharacter:
    def __init__(self, name, health=100, attack=10):
        self.name = name
        self.health = health
        self.attack = attack
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        return f"{self.name} took {damage} damage. Health: {self.health}"
    
    def attack_target(self, target):
        return target.take_damage(self.attack)
    
    def is_alive(self):
        return self.health > 0

class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=120, attack=15)
        self.armor = 5
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.armor)
        return super().take_damage(actual_damage)

class Mage(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=80, attack=20)
        self.mana = 100
    
    def cast_spell(self, target):
        if self.mana >= 25:
            self.mana -= 25
            damage = self.attack * 1.5
            return f"{self.name} casts spell! {target.take_damage(int(damage))}"
        return f"{self.name} doesn't have enough mana!"

warrior = Warrior("Conan")
mage = Mage("Gandalf")

print(f"Warrior attacks mage: {warrior.attack_target(mage)}")
print(f"Mage casts spell: {mage.cast_spell(warrior)}")

# 5. Vehicle hierarchy
print("\nExercise 5: Vehicle Hierarchy")
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

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery: {self.battery_level}%"

class GasVehicle(Vehicle):
    def __init__(self, make, model, year, fuel_capacity):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 100
    
    def refuel(self, amount):
        self.fuel_level = min(100, self.fuel_level + amount)
        return f"Fuel: {self.fuel_level}%"

class HybridVehicle(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, battery_capacity):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
        self.battery_capacity = battery_capacity
        self.fuel_level = 100
        self.battery_level = 100
    
    def refuel(self, amount):
        self.fuel_level = min(100, self.fuel_level + amount)
        return f"Fuel: {self.fuel_level}%"
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery: {self.battery_level}%"

vehicles = [
    ElectricVehicle("Tesla", "Model 3", 2023, 75),
    GasVehicle("Ford", "F-150", 2023, 36),
    HybridVehicle("Toyota", "Prius", 2023, 11.3, 1.3)
]

for vehicle in vehicles:
    print(f"{vehicle.start()}")
    if hasattr(vehicle, 'charge'):
        print(f"  {vehicle.charge(20)}")
    if hasattr(vehicle, 'refuel'):
        print(f"  {vehicle.refuel(10)}")

print("\n🎉 Congratulations! You've completed Lesson 17!")
print("Next: Lesson 18 - List Comprehensions")
