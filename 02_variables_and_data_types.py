# Lesson 2: Variables and Data Types

"""
This lesson covers:
- Variables and variable naming
- Basic data types (int, float, string, bool)
- Type conversion
- Variable assignment and reassignment
- Constants and naming conventions
"""

# 1. Variables - Containers for storing data
# Variables are created when you assign a value to them

# Creating variables
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Variables:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is student: {is_student}")

# 2. Variable Naming Rules
"""
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case sensitive
- Cannot use reserved keywords
- Use descriptive names
"""

# Valid variable names
user_name = "john_doe"
userAge = 30
_user_id = 12345
total_amount = 100.50

# Invalid variable names (commented out to avoid errors)
# 2name = "invalid"  # Cannot start with number
# user-name = "invalid"  # Cannot contain hyphens
# class = "invalid"  # Cannot use reserved keywords

print(f"Valid variables: {user_name}, {userAge}, {_user_id}, {total_amount}")

# 3. Data Types

# Integer (int) - Whole numbers
count = 42
negative_number = -10
large_number = 1000000

print(f"Integers: {count}, {negative_number}, {large_number}")
print(f"Type of count: {type(count)}")

# Float (float) - Decimal numbers
price = 19.99
pi = 3.14159
scientific = 1.23e4  # Scientific notation

print(f"Floats: {price}, {pi}, {scientific}")
print(f"Type of price: {type(price)}")

# String (str) - Text data
message = "Hello, World!"
single_quote = 'Python is awesome'
multiline = """This is a
multiline string"""

print(f"Strings: {message}, {single_quote}")
print(f"Multiline: {multiline}")
print(f"Type of message: {type(message)}")

# Boolean (bool) - True or False
is_active = True
is_completed = False

print(f"Booleans: {is_active}, {is_completed}")
print(f"Type of is_active: {type(is_active)}")

# 4. Type Conversion
# Converting between different data types

# Converting to string
number = 42
number_str = str(number)
print(f"Number as string: '{number_str}' (type: {type(number_str)})")

# Converting to integer
string_number = "123"
string_as_int = int(string_number)
print(f"String as int: {string_as_int} (type: {type(string_as_int)})")

# Converting to float
string_float = "3.14"
string_as_float = float(string_float)
print(f"String as float: {string_as_float} (type: {type(string_as_float)})")

# Converting to boolean
# Empty values are False, non-empty values are True
empty_string = ""
non_empty_string = "hello"
zero = 0
non_zero = 1

print(f"Empty string to bool: {bool(empty_string)}")
print(f"Non-empty string to bool: {bool(non_empty_string)}")
print(f"Zero to bool: {bool(zero)}")
print(f"Non-zero to bool: {bool(non_zero)}")

# 5. Variable Reassignment
# Variables can be reassigned to different values and types

x = 10
print(f"x = {x} (type: {type(x)})")

x = "Hello"
print(f"x = {x} (type: {type(x)})")

x = 3.14
print(f"x = {x} (type: {type(x)})")

# 6. Multiple Assignment
# Assigning multiple variables at once

a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Swapping variables
x, y = 10, 20
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

# 7. Constants (convention: use UPPERCASE)
# Python doesn't have true constants, but we use naming convention

PI = 3.14159
MAX_CONNECTIONS = 100
API_URL = "https://api.example.com"

print(f"Constants: PI={PI}, MAX_CONNECTIONS={MAX_CONNECTIONS}")

# 8. None Type
# Represents absence of value

empty_value = None
print(f"None value: {empty_value} (type: {type(empty_value)})")

# 9. Checking Data Types
value = 42
print(f"Is {value} an integer? {isinstance(value, int)}")
print(f"Is {value} a string? {isinstance(value, str)}")

# 10. Dynamic Typing
# Python variables can change type during execution

dynamic_var = 10
print(f"Step 1: {dynamic_var} (type: {type(dynamic_var)})")

dynamic_var = "Now I'm a string"
print(f"Step 2: {dynamic_var} (type: {type(dynamic_var)})")

dynamic_var = [1, 2, 3]
print(f"Step 3: {dynamic_var} (type: {type(dynamic_var)})")

# Exercises:
"""
1. Create variables for your name, age, and favorite color
2. Convert your age to a string and concatenate it with your name
3. Create a variable with value 0 and convert it to boolean
4. Swap the values of two variables
5. Create a constant for the speed of light (299792458)
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Create variables for your name, age, and favorite color
my_name = "Alex"
my_age = 28
favorite_color = "blue"
print(f"Name: {my_name}, Age: {my_age}, Color: {favorite_color}")

# 2. Convert your age to a string and concatenate it with your name
age_str = str(my_age)
name_age = my_name + " is " + age_str + " years old"
print(name_age)

# 3. Create a variable with value 0 and convert it to boolean
zero_value = 0
zero_bool = bool(zero_value)
print(f"Zero as boolean: {zero_bool}")

# 4. Swap the values of two variables
var1, var2 = "first", "second"
print(f"Before swap: var1={var1}, var2={var2}")
var1, var2 = var2, var1
print(f"After swap: var1={var1}, var2={var2}")

# 5. Create a constant for the speed of light
SPEED_OF_LIGHT = 299792458
print(f"Speed of light: {SPEED_OF_LIGHT} m/s")

print("\n🎉 Congratulations! You've completed Lesson 2!")
print("Next: Lesson 3 - Input and Output")
