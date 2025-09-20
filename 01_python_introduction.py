# Lesson 1: Python Introduction

"""
Welcome to Python! This lesson covers:
- What is Python
- Python installation
- Your first Python program
- Python syntax basics
- Comments and documentation
"""

# 1. What is Python?
"""
Python is a high-level, interpreted programming language known for:
- Simple and readable syntax
- Versatile (web development, data science, AI, automation)
- Large community and extensive libraries
- Cross-platform compatibility
"""

# 2. Your First Python Program
print("Hello, World!")
print("Welcome to Python programming!")

# 3. Python Syntax Basics
# - Python uses indentation to define code blocks
# - No semicolons needed at the end of lines
# - Comments start with #

# 4. Variables (we'll learn more in the next lesson)
name = "Python"
version = 3.9
is_awesome = True

print(f"Language: {name}")
print(f"Version: {version}")
print(f"Is awesome: {is_awesome}")

# 5. Comments and Documentation
# Single line comment

"""
Multi-line comment
This is also called a docstring
Used for documentation
"""

# 6. Basic Output
print("This is a simple print statement")
print("You can print", "multiple items", "separated by commas")
print("Numbers:", 42, "and", 3.14)

# 7. Escape Characters
print("This is a \"quoted\" string")
print("This is a new\nline")
print("This is a tab\tcharacter")

# 8. Raw Strings
print(r"This is a raw string\nNo escape characters processed")

# 9. String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# 10. Basic Math Operations
print("Basic math:")
print("Addition:", 5 + 3)
print("Subtraction:", 10 - 4)
print("Multiplication:", 6 * 7)
print("Division:", 15 / 3)
print("Floor division:", 15 // 4)
print("Modulus:", 15 % 4)
print("Exponentiation:", 2 ** 3)

# Exercises:
"""
1. Print your name and age
2. Print the result of 7 * 8
3. Print a message with quotes inside
4. Create a multi-line comment explaining what Python is
5. Print "Python is awesome!" using string concatenation
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Print your name and age
my_name = "Student"
my_age = 20
print(f"My name is {my_name} and I am {my_age} years old")

# 2. Print the result of 7 * 8
result = 7 * 8
print(f"7 * 8 = {result}")

# 3. Print a message with quotes inside
print('He said, "Python is amazing!"')

# 4. Multi-line comment
"""
Python is a versatile programming language that is:
- Easy to learn and read
- Used in web development, data science, AI
- Has a large community and many libraries
- Cross-platform compatible
"""

# 5. Print "Python is awesome!" using string concatenation
language = "Python"
adjective = "awesome"
message = language + " is " + adjective + "!"
print(message)

print("\n🎉 Congratulations! You've completed Lesson 1!")
print("Next: Lesson 2 - Variables and Data Types")
