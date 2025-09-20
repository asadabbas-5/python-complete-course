# Lesson 12: Function Scope

"""
This lesson covers:
- Local vs global scope
- Nonlocal keyword
- Scope resolution (LEGB rule)
- Closures and nested functions
- Global keyword usage
- Scope best practices
- Common scope-related issues
"""

# 1. Local vs Global Scope
print("=== Local vs Global Scope ===")

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

# Accessing variables
scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause NameError

# 2. Variable Shadowing
print("\n=== Variable Shadowing ===")

name = "Global Name"

def shadow_demo():
    name = "Local Name"  # This shadows the global variable
    print(f"Inside function: {name}")

print(f"Before function call: {name}")
shadow_demo()
print(f"After function call: {name}")

# 3. Global Keyword
print("\n=== Global Keyword ===")

counter = 0

def increment_counter():
    global counter  # Declare we want to modify the global variable
    counter += 1
    print(f"Counter inside function: {counter}")

def reset_counter():
    global counter
    counter = 0
    print(f"Counter reset to: {counter}")

print(f"Initial counter: {counter}")
increment_counter()
increment_counter()
print(f"Counter after increments: {counter}")
reset_counter()
print(f"Counter after reset: {counter}")

# 4. Nonlocal Keyword
print("\n=== Nonlocal Keyword ===")

def outer_function():
    outer_var = "Outer variable"
    
    def inner_function():
        nonlocal outer_var  # Access the variable from the enclosing scope
        outer_var = "Modified by inner function"
        print(f"Inner function: {outer_var}")
    
    print(f"Before inner function: {outer_var}")
    inner_function()
    print(f"After inner function: {outer_var}")

outer_function()

# 5. LEGB Rule (Local, Enclosing, Global, Built-in)
print("\n=== LEGB Rule ===")

# Built-in scope
print(f"Built-in len function: {len}")

# Global scope
global_name = "Global"

def enclosing_function():
    # Enclosing scope
    enclosing_name = "Enclosing"
    
    def local_function():
        # Local scope
        local_name = "Local"
        
        # This will access variables in LEGB order
        print(f"Local: {local_name}")
        print(f"Enclosing: {enclosing_name}")
        print(f"Global: {global_name}")
        print(f"Built-in: {len('test')}")
    
    local_function()

enclosing_function()

# 6. Closures
print("\n=== Closures ===")

def create_multiplier(factor):
    """Create a closure that multiplies by a factor"""
    def multiplier(number):
        return number * factor
    return multiplier

# Create closures with different factors
double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")
print(f"Quadruple 5: {quadruple(5)}")

# Closure with mutable state
def create_counter():
    """Create a counter closure"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = create_counter()
counter2 = create_counter()

print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter2: {counter2()}, {counter2()}")

# 7. Nested Functions
print("\n=== Nested Functions ===")

def outer_function(x):
    """Outer function with nested functions"""
    
    def inner_function(y):
        """Inner function that uses outer function's variable"""
        return x + y
    
    def another_inner(z):
        """Another inner function"""
        return x * z
    
    # Return both inner functions
    return inner_function, another_inner

# Get the inner functions
add_func, multiply_func = outer_function(10)

print(f"Add 5 to 10: {add_func(5)}")
print(f"Multiply 3 by 10: {multiply_func(3)}")

# 8. Scope in Classes
print("\n=== Scope in Classes ===")

class ScopeDemo:
    # Class variable (shared by all instances)
    class_var = "I'm a class variable"
    
    def __init__(self, instance_var):
        # Instance variable (unique to each instance)
        self.instance_var = instance_var
    
    def instance_method(self):
        # Method can access instance and class variables
        print(f"Instance variable: {self.instance_var}")
        print(f"Class variable: {self.class_var}")
    
    @classmethod
    def class_method(cls):
        # Class method can access class variables
        print(f"Class variable from class method: {cls.class_var}")
    
    @staticmethod
    def static_method():
        # Static method cannot access instance or class variables
        print("I'm a static method")

# Test class scope
obj1 = ScopeDemo("Instance 1")
obj2 = ScopeDemo("Instance 2")

obj1.instance_method()
obj2.instance_method()

ScopeDemo.class_method()
ScopeDemo.static_method()

# 9. Scope with Lambda Functions
print("\n=== Scope with Lambda Functions ===")

def create_lambda_functions():
    """Create lambda functions with different scopes"""
    
    # Lambda with local scope
    local_lambda = lambda x: x * 2
    
    # Lambda that captures enclosing scope
    factor = 3
    enclosing_lambda = lambda x: x * factor
    
    return local_lambda, enclosing_lambda

local_func, enclosing_func = create_lambda_functions()

print(f"Local lambda (5 * 2): {local_func(5)}")
print(f"Enclosing lambda (5 * 3): {enclosing_func(5)}")

# 10. Scope Issues and Solutions
print("\n=== Scope Issues and Solutions ===")

# Common issue: Late binding in loops
def create_functions():
    """Demonstrate late binding issue"""
    functions = []
    for i in range(3):
        functions.append(lambda: i)  # All functions will return 2
    return functions

# This will print 2, 2, 2 (not 0, 1, 2)
problematic_funcs = create_functions()
print("Late binding issue:")
for func in problematic_funcs:
    print(func())

# Solution: Capture the value immediately
def create_functions_fixed():
    """Fixed version using default parameters"""
    functions = []
    for i in range(3):
        functions.append(lambda i=i: i)  # Capture i immediately
    return functions

fixed_funcs = create_functions_fixed()
print("Fixed version:")
for func in fixed_funcs:
    print(func())

# 11. Scope Best Practices
print("\n=== Scope Best Practices ===")

# 1. Minimize global variables
class Configuration:
    """Better than global variables"""
    def __init__(self):
        self.debug = False
        self.port = 8080
        self.host = "localhost"

config = Configuration()

def process_request():
    """Function that uses configuration"""
    if config.debug:
        print("Debug mode enabled")
    return f"Processing on {config.host}:{config.port}"

print(process_request())

# 2. Use closures for stateful functions
def create_validator(min_length=8):
    """Create a validator with configurable minimum length"""
    def validate_password(password):
        return len(password) >= min_length
    return validate_password

# Create different validators
short_validator = create_validator(4)
long_validator = create_validator(12)

print(f"Short validator ('test'): {short_validator('test')}")
print(f"Long validator ('test'): {long_validator('test')}")
print(f"Long validator ('password123'): {long_validator('password123')}")

# 3. Use nonlocal for nested function communication
def create_accumulator():
    """Create an accumulator using nonlocal"""
    total = 0
    
    def add(value):
        nonlocal total
        total += value
        return total
    
    def get_total():
        return total
    
    def reset():
        nonlocal total
        total = 0
    
    return add, get_total, reset

add_func, get_total_func, reset_func = create_accumulator()

print(f"Add 5: {add_func(5)}")
print(f"Add 3: {add_func(3)}")
print(f"Total: {get_total_func()}")
reset_func()
print(f"After reset: {get_total_func()}")

# 12. Advanced Scope Examples
print("\n=== Advanced Scope Examples ===")

# Example 1: Function Factory with State
def create_function_factory():
    """Create functions with shared state"""
    shared_state = {"count": 0, "last_value": None}
    
    def increment():
        shared_state["count"] += 1
        return shared_state["count"]
    
    def set_last_value(value):
        shared_state["last_value"] = value
    
    def get_state():
        return shared_state.copy()
    
    return increment, set_last_value, get_state

inc_func, set_func, get_state_func = create_function_factory()

print(f"Increment: {inc_func()}")
print(f"Increment: {inc_func()}")
set_func("Hello")
print(f"State: {get_state_func()}")

# Example 2: Decorator with Scope
def scope_tracking_decorator(func):
    """Decorator that tracks function calls using closure"""
    call_count = 0
    last_args = None
    last_kwargs = None
    
    def wrapper(*args, **kwargs):
        nonlocal call_count, last_args, last_kwargs
        call_count += 1
        last_args = args
        last_kwargs = kwargs
        
        print(f"Function {func.__name__} called {call_count} times")
        print(f"Last args: {last_args}, Last kwargs: {last_kwargs}")
        
        return func(*args, **kwargs)
    
    # Add methods to access closure state
    wrapper.get_call_count = lambda: call_count
    wrapper.get_last_args = lambda: last_args
    wrapper.get_last_kwargs = lambda: last_kwargs
    
    return wrapper

@scope_tracking_decorator
def example_function(x, y, z=10):
    return x + y + z

result1 = example_function(1, 2)
result2 = example_function(3, 4, z=5)

print(f"Call count: {example_function.get_call_count()}")
print(f"Last args: {example_function.get_last_args()}")

# Example 3: Module-level Scope Management
class ScopeManager:
    """Manage scope at module level"""
    _instances = {}
    
    @classmethod
    def get_instance(cls, name):
        if name not in cls._instances:
            cls._instances[name] = cls()
        return cls._instances[name]
    
    def __init__(self):
        self.data = {}
    
    def set_data(self, key, value):
        self.data[key] = value
    
    def get_data(self, key):
        return self.data.get(key)

# Use scope manager
manager1 = ScopeManager.get_instance("config")
manager2 = ScopeManager.get_instance("cache")

manager1.set_data("debug", True)
manager2.set_data("max_size", 100)

print(f"Config debug: {manager1.get_data('debug')}")
print(f"Cache max_size: {manager2.get_data('max_size')}")

# Exercises:
"""
1. Create a closure that remembers a list and provides methods to add/remove items
2. Write a function that creates a counter with increment, decrement, and reset methods
3. Create a decorator that tracks the number of times a function is called
4. Write a function that creates a simple state machine using closures
5. Create a function that implements a simple cache using closures
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. List manager closure
print("Exercise 1: List Manager Closure")
def create_list_manager():
    items = []
    
    def add_item(item):
        items.append(item)
        return items.copy()
    
    def remove_item(item):
        if item in items:
            items.remove(item)
        return items.copy()
    
    def get_items():
        return items.copy()
    
    def clear():
        items.clear()
    
    return add_item, remove_item, get_items, clear

add, remove, get_all, clear_all = create_list_manager()

print(f"Add 'apple': {add('apple')}")
print(f"Add 'banana': {add('banana')}")
print(f"Remove 'apple': {remove('apple')}")
print(f"Current items: {get_all()}")

# 2. Counter with methods
print("\nExercise 2: Counter with Methods")
def create_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def reset():
        nonlocal count
        count = 0
        return count
    
    def get_count():
        return count
    
    return increment, decrement, reset, get_count

inc, dec, reset, get_count = create_counter()

print(f"Increment: {inc()}")
print(f"Increment: {inc()}")
print(f"Decrement: {dec()}")
print(f"Current count: {get_count()}")
print(f"Reset: {reset()}")

# 3. Call tracking decorator
print("\nExercise 3: Call Tracking Decorator")
def track_calls(func):
    call_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"{func.__name__} called {call_count} times")
        return func(*args, **kwargs)
    
    wrapper.get_call_count = lambda: call_count
    return wrapper

@track_calls
def multiply(x, y):
    return x * y

multiply(2, 3)
multiply(4, 5)
print(f"Total calls: {multiply.get_call_count()}")

# 4. Simple state machine
print("\nExercise 4: Simple State Machine")
def create_state_machine():
    current_state = "idle"
    
    def set_state(new_state):
        nonlocal current_state
        current_state = new_state
        print(f"State changed to: {current_state}")
    
    def get_state():
        return current_state
    
    def process_event(event):
        nonlocal current_state
        if current_state == "idle" and event == "start":
            current_state = "running"
        elif current_state == "running" and event == "stop":
            current_state = "stopped"
        elif current_state == "stopped" and event == "reset":
            current_state = "idle"
        else:
            print(f"Invalid event '{event}' for state '{current_state}'")
        print(f"Current state: {current_state}")
    
    return set_state, get_state, process_event

set_state, get_state, process_event = create_state_machine()

process_event("start")
process_event("stop")
process_event("reset")

# 5. Simple cache
print("\nExercise 5: Simple Cache")
def create_cache():
    cache = {}
    
    def get(key):
        return cache.get(key)
    
    def set(key, value):
        cache[key] = value
    
    def clear():
        cache.clear()
    
    def size():
        return len(cache)
    
    def keys():
        return list(cache.keys())
    
    return get, set, clear, size, keys

get_cache, set_cache, clear_cache, cache_size, cache_keys = create_cache()

set_cache("user1", "Alice")
set_cache("user2", "Bob")
print(f"Cache size: {cache_size()}")
print(f"Cache keys: {cache_keys()}")
print(f"Get user1: {get_cache('user1')}")

print("\n🎉 Congratulations! You've completed Lesson 12!")
print("Next: Lesson 13 - File Handling")
