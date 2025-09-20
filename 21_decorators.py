# Lesson 21: Decorators

"""
This lesson covers:
- What are decorators
- Function decorators
- Class decorators
- Decorator with parameters
- Multiple decorators
- Built-in decorators (@property, @staticmethod, @classmethod)
- Decorator patterns and best practices
- Practical decorator examples
"""

# 1. What are Decorators
print("=== What are Decorators ===")

# Decorators are functions that modify or enhance other functions
# They allow you to add functionality to existing functions without modifying them

def my_decorator(func):
    """A simple decorator"""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()

# 2. Function Decorators
print("\n=== Function Decorators ===")

# Decorator for timing functions
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

# Decorator for logging
def log_decorator(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)

# 3. Decorator with Parameters
print("\n=== Decorator with Parameters ===")

def repeat(times):
    """Decorator that repeats a function a specified number of times"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Call {i + 1}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Decorator with conditional execution
def conditional_decorator(condition):
    """Decorator that only executes if condition is True"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(f"Condition is True, executing {func.__name__}")
                return func(*args, **kwargs)
            else:
                print(f"Condition is False, skipping {func.__name__}")
                return None
        return wrapper
    return decorator

@conditional_decorator(True)
def important_function():
    print("This is important!")

@conditional_decorator(False)
def skipped_function():
    print("This will be skipped!")

important_function()
skipped_function()

# 4. Multiple Decorators
print("\n=== Multiple Decorators ===")

def bold_decorator(func):
    """Make function output bold"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic_decorator(func):
    """Make function output italic"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

@bold_decorator
@italic_decorator
def get_message():
    return "Hello, World!"

print(f"Decorated message: {get_message()}")

# Order matters - decorators are applied from bottom to top
@italic_decorator
@bold_decorator
def get_message_reversed():
    return "Hello, World!"

print(f"Reversed order: {get_message_reversed()}")

# 5. Class Decorators
print("\n=== Class Decorators ===")

def singleton(cls):
    """Singleton decorator for classes"""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection_id = id(self)
        print(f"Database connection created: {self.connection_id}")
    
    def query(self, sql):
        return f"Executing: {sql}"

# Test singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")

# Decorator to add methods to a class
def add_methods(*methods):
    """Decorator to add methods to a class"""
    def decorator(cls):
        for method_name, method_func in methods:
            setattr(cls, method_name, method_func)
        return cls
    return decorator

def greet_method(self):
    return f"Hello from {self.__class__.__name__}!"

def info_method(self):
    return f"This is {self.__class__.__name__}"

@add_methods(('greet', greet_method), ('info', info_method))
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.greet())
print(person.info())

# 6. Built-in Decorators
print("\n=== Built-in Decorators ===")

# @property decorator
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

# @staticmethod decorator
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a + b

print(f"Static method: {MathUtils.add(5, 3)}")

# @classmethod decorator
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    
    @classmethod
    def get_population(cls):
        return cls.population
    
    @classmethod
    def create_baby(cls, name):
        return cls(f"Baby {name}")

person1 = Person("Alice")
person2 = Person("Bob")
baby = Person.create_baby("Charlie")

print(f"Population: {Person.get_population()}")

# 7. Decorator Patterns
print("\n=== Decorator Patterns ===")

# Retry decorator
def retry(max_attempts=3, delay=1):
    """Decorator to retry a function on failure"""
    import time
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def unreliable_function():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("Random failure")
    return "Success!"

try:
    result = unreliable_function()
    print(f"Function result: {result}")
except Exception as e:
    print(f"All retries failed: {e}")

# Cache decorator
def cache(func):
    """Simple cache decorator"""
    cache_dict = {}
    
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache_dict:
            print(f"Cache hit for {func.__name__}")
            return cache_dict[key]
        
        result = func(*args, **kwargs)
        cache_dict[key] = result
        print(f"Cache miss for {func.__name__}")
        return result
    
    return wrapper

@cache
def expensive_function(n):
    """Simulate expensive computation"""
    import time
    time.sleep(0.1)  # Simulate work
    return n * n

print(f"First call: {expensive_function(5)}")
print(f"Second call: {expensive_function(5)}")

# 8. Decorator with functools.wraps
print("\n=== Decorator with functools.wraps ===")

from functools import wraps

def preserve_metadata(func):
    """Decorator that preserves function metadata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def example_function():
    """This is an example function"""
    return "Hello!"

print(f"Function name: {example_function.__name__}")
print(f"Function docstring: {example_function.__doc__}")

# Without @wraps, metadata would be lost
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def another_function():
    """Another example function"""
    return "World!"

print(f"Function name (bad): {another_function.__name__}")
print(f"Function docstring (bad): {another_function.__doc__}")

# 9. Practical Decorator Examples
print("\n=== Practical Decorator Examples ===")

# Authentication decorator
def require_auth(func):
    """Decorator to require authentication"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Simulate authentication check
        is_authenticated = True  # In real app, this would check session/token
        
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            return "Authentication required"
    return wrapper

@require_auth
def protected_function():
    return "This is protected content"

print(f"Protected function: {protected_function()}")

# Rate limiting decorator
def rate_limit(calls_per_minute=60):
    """Decorator to limit function calls"""
    import time
    from collections import defaultdict
    
    calls = defaultdict(list)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            minute = int(now // 60)
            
            # Clean old calls
            calls[func.__name__] = [call_time for call_time in calls[func.__name__] 
                                  if int(call_time // 60) == minute]
            
            if len(calls[func.__name__]) >= calls_per_minute:
                return "Rate limit exceeded"
            
            calls[func.__name__].append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_minute=2)
def limited_function():
    return "Function executed"

print(f"Limited function: {limited_function()}")
print(f"Limited function: {limited_function()}")
print(f"Limited function: {limited_function()}")

# Validation decorator
def validate_types(*expected_types):
    """Decorator to validate function argument types"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} must be {expected_type.__name__}, got {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, str)
def process_data(number, text):
    return f"Processing {number} and {text}"

try:
    result = process_data(42, "hello")
    print(f"Validation passed: {result}")
except TypeError as e:
    print(f"Validation failed: {e}")

# 10. Advanced Decorator Patterns
print("\n=== Advanced Decorator Patterns ===")

# Decorator factory
def decorator_factory(prefix="[INFO]"):
    """Factory function that creates decorators"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix} Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{prefix} {func.__name__} completed")
            return result
        return wrapper
    return decorator

@decorator_factory("[DEBUG]")
def debug_function():
    return "Debug function executed"

@decorator_factory("[ERROR]")
def error_function():
    return "Error function executed"

debug_function()
error_function()

# Context manager decorator
def context_manager(func):
    """Decorator that makes a function work as a context manager"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return ContextManager(func, *args, **kwargs)
    return wrapper

class ContextManager:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def __enter__(self):
        print("Entering context")
        return self.func(*self.args, **self.kwargs)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False

@context_manager
def resource_function():
    print("Resource acquired")
    return "resource"

with resource_function() as resource:
    print(f"Using {resource}")

# 11. Decorator Best Practices
print("\n=== Decorator Best Practices ===")

# Best Practice 1: Always use @wraps
from functools import wraps

def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Best Practice 2: Handle exceptions properly
def safe_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            raise
    return wrapper

# Best Practice 3: Use decorator factories for parameterized decorators
def parameterized_decorator(param1, param2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Using parameters: {param1}, {param2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Best Practice 4: Document decorators properly
def documented_decorator(func):
    """
    A decorator that adds documentation.
    
    Args:
        func: The function to be decorated
    
    Returns:
        The decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# 12. Real-world Decorator Examples
print("\n=== Real-world Decorator Examples ===")

# API endpoint decorator
def api_endpoint(method="GET", path="/"):
    """Decorator for API endpoints"""
    def decorator(func):
        func._api_method = method
        func._api_path = path
        return func
    return decorator

@api_endpoint(method="GET", path="/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@api_endpoint(method="POST", path="/users")
def create_user():
    return {"message": "User created"}

print(f"Get users endpoint: {get_users._api_method} {get_users._api_path}")
print(f"Create user endpoint: {create_user._api_method} {create_user._api_path}")

# Database transaction decorator
def database_transaction(func):
    """Decorator for database transactions"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting database transaction")
        try:
            result = func(*args, **kwargs)
            print("Committing transaction")
            return result
        except Exception as e:
            print("Rolling back transaction")
            raise e
    return wrapper

@database_transaction
def save_user(user_data):
    print(f"Saving user: {user_data}")
    return "User saved"

save_user({"name": "Alice", "email": "alice@example.com"})

# Exercises:
"""
1. Create a decorator that measures the execution time of a function
2. Write a decorator that logs function calls with timestamps
3. Create a decorator that retries a function on failure
4. Write a decorator that caches function results
5. Create a decorator that validates function arguments
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Execution time decorator
print("Exercise 1: Execution Time Decorator")
def measure_time(func):
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_calculation(n):
    total = sum(range(n))
    return total

result = slow_calculation(1000000)

# 2. Logging decorator
print("\nExercise 2: Logging Decorator")
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] {func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add_numbers(a, b):
    return a + b

add_numbers(5, 3)

# 3. Retry decorator
print("\nExercise 3: Retry Decorator")
def retry_on_failure(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            return None
        return wrapper
    return decorator

@retry_on_failure(max_retries=3)
def unreliable_operation():
    import random
    if random.random() < 0.7:
        raise Exception("Operation failed")
    return "Operation successful"

try:
    result = unreliable_operation()
    print(f"Result: {result}")
except Exception as e:
    print(f"All retries failed: {e}")

# 4. Cache decorator
print("\nExercise 4: Cache Decorator")
def cache_results(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            print(f"Cache hit for {func.__name__}")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"Cache miss for {func.__name__}")
        return result
    return wrapper

@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci(10): {fibonacci(10)}")

# 5. Validation decorator
print("\nExercise 5: Validation Decorator")
def validate_args(*expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} must be {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_args(int, str, float)
def process_data(number, text, value):
    return f"Processing {number}, {text}, {value}"

try:
    result = process_data(42, "hello", 3.14)
    print(f"Validation passed: {result}")
except TypeError as e:
    print(f"Validation failed: {e}")

print("\n🎉 Congratulations! You've completed Lesson 21!")
print("Next: Lesson 22 - Generators")
