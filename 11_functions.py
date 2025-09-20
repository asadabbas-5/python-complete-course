# Lesson 11: Functions

"""
This lesson covers:
- Function definition and calling
- Parameters and arguments
- Return values
- Default parameters
- Variable-length arguments
- Lambda functions
- Function scope and closures
- Decorators basics
"""

# 1. Basic Function Definition and Calling
print("=== Basic Function Definition and Calling ===")

def greet():
    """Simple function that prints a greeting"""
    print("Hello, World!")

def greet_person(name):
    """Function that takes a parameter"""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Function that takes parameters and returns a value"""
    return a + b

# Calling functions
greet()
greet_person("Alice")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 2. Parameters and Arguments
print("\n=== Parameters and Arguments ===")

def calculate_area(length, width):
    """Calculate area of a rectangle"""
    return length * width

def calculate_volume(length, width, height):
    """Calculate volume of a box"""
    return length * width * height

# Positional arguments
area = calculate_area(10, 5)
print(f"Area: {area}")

# Keyword arguments
volume = calculate_volume(length=10, width=5, height=3)
print(f"Volume: {volume}")

# Mixed positional and keyword arguments
volume2 = calculate_volume(10, width=5, height=3)
print(f"Volume 2: {volume2}")

# 3. Default Parameters
print("\n=== Default Parameters ===")

def greet_with_title(name, title="Mr."):
    """Function with default parameter"""
    return f"Hello, {title} {name}!"

def create_user(name, age=18, is_active=True):
    """Function with multiple default parameters"""
    return {
        "name": name,
        "age": age,
        "is_active": is_active
    }

# Using default parameters
greeting1 = greet_with_title("Smith")
greeting2 = greet_with_title("Johnson", "Dr.")

print(f"Greeting 1: {greeting1}")
print(f"Greeting 2: {greeting2}")

user1 = create_user("Alice")
user2 = create_user("Bob", 25)
user3 = create_user("Charlie", 30, False)

print(f"User 1: {user1}")
print(f"User 2: {user2}")
print(f"User 3: {user3}")

# 4. Variable-Length Arguments
print("\n=== Variable-Length Arguments ===")

def sum_numbers(*args):
    """Function that accepts variable number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

def print_info(**kwargs):
    """Function that accepts keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def flexible_function(*args, **kwargs):
    """Function that accepts both positional and keyword arguments"""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

# Using variable-length arguments
total1 = sum_numbers(1, 2, 3)
total2 = sum_numbers(1, 2, 3, 4, 5)
print(f"Sum 1: {total1}")
print(f"Sum 2: {total2}")

print_info(name="Alice", age=25, city="New York")

flexible_function(1, 2, 3, name="Alice", age=25)

# 5. Return Values and Multiple Returns
print("\n=== Return Values and Multiple Returns ===")

def get_name_and_age():
    """Function that returns multiple values"""
    return "Alice", 25

def divide_numbers(a, b):
    """Function that returns different values based on condition"""
    if b == 0:
        return None, "Error: Division by zero"
    return a / b, "Success"

def find_max_min(numbers):
    """Function that returns multiple values"""
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

# Using return values
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

result, message = divide_numbers(10, 2)
print(f"10 / 2 = {result}, Message: {message}")

result, message = divide_numbers(10, 0)
print(f"10 / 0 = {result}, Message: {message}")

numbers = [3, 7, 2, 9, 1]
max_num, min_num = find_max_min(numbers)
print(f"Numbers: {numbers}")
print(f"Max: {max_num}, Min: {min_num}")

# 6. Lambda Functions
print("\n=== Lambda Functions ===")

# Basic lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Lambda with higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Sort with lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students sorted by grade: {sorted_by_grade}")

# 7. Function Scope and Closures
print("\n=== Function Scope and Closures ===")

# Global and local scope
global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variables
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

print(f"Counter before: {counter}")
increment_counter()
increment_counter()
print(f"Counter after: {counter}")

# Closures
def create_multiplier(factor):
    """Function that returns a closure"""
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# 8. Function Documentation and Type Hints
print("\n=== Function Documentation and Type Hints ===")

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius ** 2

# Using the documented function
try:
    area = calculate_circle_area(5.0)
    print(f"Circle area: {area:.2f}")
    
    # This will raise an error
    # area = calculate_circle_area(-5.0)
except ValueError as e:
    print(f"Error: {e}")

# 9. Recursive Functions
print("\n=== Recursive Functions ===")

def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def countdown(n):
    """Countdown using recursion"""
    if n <= 0:
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)

# Using recursive functions
print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci sequence:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

print("Countdown:")
countdown(5)

# 10. Higher-Order Functions
print("\n=== Higher-Order Functions ===")

def apply_operation(numbers, operation):
    """Apply an operation to a list of numbers"""
    return [operation(x) for x in numbers]

def create_operation(operation_type):
    """Create different operations based on type"""
    if operation_type == "square":
        return lambda x: x ** 2
    elif operation_type == "double":
        return lambda x: x * 2
    elif operation_type == "increment":
        return lambda x: x + 1
    else:
        return lambda x: x

numbers = [1, 2, 3, 4, 5]

# Apply different operations
squared = apply_operation(numbers, lambda x: x ** 2)
doubled = apply_operation(numbers, lambda x: x * 2)

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")

# Using operation factory
square_op = create_operation("square")
double_op = create_operation("double")

result1 = apply_operation(numbers, square_op)
result2 = apply_operation(numbers, double_op)

print(f"Using factory - Squared: {result1}")
print(f"Using factory - Doubled: {result2}")

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Calculator
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

# Test calculator
calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"History: {calc.get_history()}")

# Example 2: Data Processing Pipeline
def process_data(data, *processors):
    """Apply multiple processing functions to data"""
    result = data
    for processor in processors:
        result = processor(result)
    return result

def clean_text(text):
    """Clean text data"""
    return text.strip().lower()

def remove_punctuation(text):
    """Remove punctuation from text"""
    import re
    return re.sub(r'[^\w\s]', '', text)

def split_words(text):
    """Split text into words"""
    return text.split()

# Test data processing pipeline
raw_text = "  Hello, World! How are you?  "
processed = process_data(raw_text, clean_text, remove_punctuation, split_words)
print(f"Raw text: '{raw_text}'")
print(f"Processed: {processed}")

# Example 3: Function Decorators (Basic)
def timing_decorator(func):
    """Decorator to measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@timing_decorator
def slow_function(n):
    """A function that takes some time to execute"""
    total = 0
    for i in range(n):
        total += i
    return total

result = slow_function(1000000)
print(f"Result: {result}")

# 12. Best Practices
print("\n=== Best Practices ===")

# 1. Use descriptive function names
def calculate_monthly_payment(principal, annual_rate, years):
    """Calculate monthly mortgage payment"""
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    
    payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return payment

# 2. Keep functions small and focused
def validate_email(email):
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_email(to_email, subject, body):
    """Send email (simplified)"""
    if not validate_email(to_email):
        raise ValueError("Invalid email format")
    print(f"Email sent to {to_email}: {subject}")

# 3. Use type hints for better code clarity
def process_user_data(name: str, age: int, email: str) -> dict:
    """Process user data and return formatted dictionary"""
    return {
        "name": name.title(),
        "age": age,
        "email": email.lower(),
        "is_adult": age >= 18
    }

# Test best practices
payment = calculate_monthly_payment(200000, 4.5, 30)
print(f"Monthly payment: ${payment:.2f}")

user_data = process_user_data("alice smith", 25, "ALICE@EXAMPLE.COM")
print(f"Processed user data: {user_data}")

# Exercises:
"""
1. Write a function that checks if a number is prime
2. Create a function that converts temperature between Celsius and Fahrenheit
3. Write a function that finds the greatest common divisor of two numbers
4. Create a function that generates a list of random numbers
5. Write a function that validates a password based on criteria
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Prime number checker
print("Exercise 1: Prime Number Checker")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

test_numbers = [2, 3, 4, 5, 17, 25, 29]
for num in test_numbers:
    print(f"{num} is prime: {is_prime(num)}")

# 2. Temperature converter
print("\nExercise 2: Temperature Converter")
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return temp * 9/5 + 32
    elif from_unit == "F" and to_unit == "C":
        return (temp - 32) * 5/9
    elif from_unit == to_unit:
        return temp
    else:
        raise ValueError("Unsupported conversion")

celsius = 25
fahrenheit = convert_temperature(celsius, "C", "F")
print(f"{celsius}°C = {fahrenheit}°F")

# 3. Greatest common divisor
print("\nExercise 3: Greatest Common Divisor")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"GCD of 48 and 18: {gcd(48, 18)}")
print(f"GCD of 100 and 25: {gcd(100, 25)}")

# 4. Random number generator
print("\nExercise 4: Random Number Generator")
import random

def generate_random_numbers(count, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(count)]

random_nums = generate_random_numbers(5, 1, 50)
print(f"Random numbers: {random_nums}")

# 5. Password validator
print("\nExercise 5: Password Validator")
def validate_password(password):
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter")
    
    if not any(c.islower() for c in password):
        errors.append("Password must contain at least one lowercase letter")
    
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one digit")
    
    if not any(c in "!@#$%^&*()" for c in password):
        errors.append("Password must contain at least one special character")
    
    return len(errors) == 0, errors

test_passwords = ["weak", "Strong123", "MyPassword123!"]
for pwd in test_passwords:
    is_valid, errors = validate_password(pwd)
    print(f"'{pwd}': {'Valid' if is_valid else 'Invalid'}")
    if errors:
        for error in errors:
            print(f"  - {error}")

print("\n🎉 Congratulations! You've completed Lesson 11!")
print("Next: Lesson 12 - Function Scope")
