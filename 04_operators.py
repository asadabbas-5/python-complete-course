# Lesson 4: Operators

"""
This lesson covers:
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
- Bitwise operators
- Operator precedence
- Special operators (identity, membership)
"""

# 1. Arithmetic Operators
print("=== Arithmetic Operators ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# 2. Comparison Operators
print("\n=== Comparison Operators ===")

x = 5
y = 8

print(f"x = {x}, y = {y}")
print(f"Equal (x == y): {x == y}")
print(f"Not equal (x != y): {x != y}")
print(f"Less than (x < y): {x < y}")
print(f"Greater than (x > y): {x > y}")
print(f"Less than or equal (x <= y): {x <= y}")
print(f"Greater than or equal (x >= y): {x >= y}")

# String comparison
name1 = "Alice"
name2 = "Bob"
print(f"String comparison: '{name1}' < '{name2}': {name1 < name2}")

# 3. Logical Operators
print("\n=== Logical Operators ===")

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"AND (p and q): {p and q}")
print(f"OR (p or q): {p or q}")
print(f"NOT (not p): {not p}")
print(f"NOT (not q): {not q}")

# Short-circuit evaluation
def check_value(x):
    print(f"Checking value: {x}")
    return x > 0

print("Short-circuit AND:")
result1 = check_value(5) and check_value(0)  # Second function won't be called
print(f"Result: {result1}")

print("Short-circuit OR:")
result2 = check_value(5) or check_value(0)   # Second function won't be called
print(f"Result: {result2}")

# 4. Assignment Operators
print("\n=== Assignment Operators ===")

num = 10
print(f"Initial value: {num}")

num += 5    # num = num + 5
print(f"After += 5: {num}")

num -= 3    # num = num - 3
print(f"After -= 3: {num}")

num *= 2    # num = num * 2
print(f"After *= 2: {num}")

num /= 4    # num = num / 4
print(f"After /= 4: {num}")

num //= 2   # num = num // 2
print(f"After //= 2: {num}")

num %= 3    # num = num % 3
print(f"After %= 3: {num}")

num **= 2   # num = num ** 2
print(f"After **= 2: {num}")

# 5. Bitwise Operators
print("\n=== Bitwise Operators ===")

a = 12  # Binary: 1100
b = 10  # Binary: 1010

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")
print(f"AND (a & b): {a & b} (binary: {bin(a & b)})")
print(f"OR (a | b): {a | b} (binary: {bin(a | b)})")
print(f"XOR (a ^ b): {a ^ b} (binary: {bin(a ^ b)})")
print(f"NOT (~a): {~a} (binary: {bin(~a)})")
print(f"Left shift (a << 2): {a << 2} (binary: {bin(a << 2)})")
print(f"Right shift (a >> 2): {a >> 2} (binary: {bin(a >> 2)})")

# 6. Identity Operators
print("\n=== Identity Operators ===")

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"x is y: {x is y}")      # False (different objects)
print(f"x is z: {x is z}")      # True (same object)
print(f"x is not y: {x is not y}")  # True
print(f"x == y: {x == y}")      # True (same values)

# 7. Membership Operators
print("\n=== Membership Operators ===")

fruits = ["apple", "banana", "cherry"]
text = "Hello, World!"

print(f"fruits = {fruits}")
print(f"text = '{text}'")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")
print(f"'World' in text: {'World' in text}")
print(f"'Python' in text: {'Python' in text}")

# 8. Operator Precedence
print("\n=== Operator Precedence ===")

# Example showing precedence
result = 2 + 3 * 4 ** 2
print(f"2 + 3 * 4 ** 2 = {result}")
print("Order: ** (exponentiation) first, then * (multiplication), then + (addition)")

# Using parentheses to change precedence
result2 = (2 + 3) * 4 ** 2
print(f"(2 + 3) * 4 ** 2 = {result2}")

# Precedence table (highest to lowest)
print("\nOperator Precedence (highest to lowest):")
print("1. ** (exponentiation)")
print("2. +x, -x, ~x (unary operators)")
print("3. *, /, //, % (multiplication, division)")
print("4. +, - (addition, subtraction)")
print("5. <<, >> (bitwise shifts)")
print("6. & (bitwise AND)")
print("7. ^ (bitwise XOR)")
print("8. | (bitwise OR)")
print("9. ==, !=, <, >, <=, >= (comparison)")
print("10. is, is not (identity)")
print("11. in, not in (membership)")
print("12. not (logical NOT)")
print("13. and (logical AND)")
print("14. or (logical OR)")

# 9. Chained Comparisons
print("\n=== Chained Comparisons ===")

age = 25
print(f"age = {age}")
print(f"18 <= age <= 65: {18 <= age <= 65}")
print(f"age < 18 or age > 65: {age < 18 or age > 65}")

# Multiple chained comparisons
x, y, z = 5, 10, 15
print(f"x = {x}, y = {y}, z = {z}")
print(f"x < y < z: {x < y < z}")
print(f"x < y and y < z: {x < y and y < z}")  # Equivalent

# 10. Walrus Operator (Python 3.8+)
print("\n=== Walrus Operator (:=) ===")

# Assignment expression - assigns and returns value
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}")

# Using walrus operator in while loop
n = 0
while (current := numbers[n]) < 4:
    print(f"Current number: {current}")
    n += 1

# Using walrus operator in list comprehension
squares = [square := x**2 for x in range(5)]
print(f"Squares: {squares}")

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Calculator function
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Test calculator
print("Calculator examples:")
print(f"5 + 3 = {calculator(5, 3, '+')}")
print(f"10 - 4 = {calculator(10, 4, '-')}")
print(f"6 * 7 = {calculator(6, 7, '*')}")
print(f"15 / 3 = {calculator(15, 3, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")

# Number classification
def classify_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

print(f"\nNumber classification:")
print(f"5 is {classify_number(5)}")
print(f"-3 is {classify_number(-3)}")
print(f"0 is {classify_number(0)}")

# Exercises:
"""
1. Calculate the area of a circle (π * r²) where r = 5
2. Check if a number is even or odd using modulo operator
3. Create a program that determines if a year is a leap year
4. Use bitwise operators to check if a number is a power of 2
5. Write a program that swaps two numbers without using a temporary variable
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Circle area
print("Exercise 1: Circle Area")
import math
radius = 5
area = math.pi * radius ** 2
print(f"Area of circle with radius {radius}: {area:.2f}")

# 2. Even or odd
print("\nExercise 2: Even or Odd")
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 3. Leap year
print("\nExercise 3: Leap Year")
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is {'a leap year' if is_leap else 'not a leap year'}")

# 4. Power of 2
print("\nExercise 4: Power of 2")
num = 16
is_power_of_2 = num > 0 and (num & (num - 1)) == 0
print(f"{num} is {'a power of 2' if is_power_of_2 else 'not a power of 2'}")

# 5. Swap without temporary variable
print("\nExercise 5: Swap Numbers")
a, b = 10, 20
print(f"Before swap: a = {a}, b = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swap: a = {a}, b = {b}")

print("\n🎉 Congratulations! You've completed Lesson 4!")
print("Next: Lesson 5 - Control Flow")
