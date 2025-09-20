# Lesson 3: Input and Output

"""
This lesson covers:
- Getting user input with input()
- Displaying output with print()
- String formatting methods
- File input/output basics
- Error handling for input
"""

# 1. Getting User Input
# The input() function gets text from the user

print("=== Getting User Input ===")

# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input with type conversion
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Multiple inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Full name: {first_name} {last_name}")

# 2. Input with Error Handling
print("\n=== Input with Error Handling ===")

def get_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Please enter a valid number!")

# Example usage
user_number = get_number()
print(f"You entered: {user_number}")

# 3. String Formatting Methods
print("\n=== String Formatting ===")

name = "Alice"
age = 25
height = 5.6

# Method 1: f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}, Height: {height}")

# Method 2: .format() method
print("Name: {}, Age: {}, Height: {}".format(name, age, height))
print("Name: {0}, Age: {1}, Height: {2}".format(name, age, height))
print("Name: {n}, Age: {a}, Height: {h}".format(n=name, a=age, h=height))

# Method 3: % formatting (older style)
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

# 4. Advanced String Formatting
print("\n=== Advanced String Formatting ===")

# Number formatting
pi = 3.14159
print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Pi in scientific notation: {pi:.2e}")

# Padding and alignment
text = "Hello"
print(f"Left aligned: '{text:<10}'")
print(f"Right aligned: '{text:>10}'")
print(f"Center aligned: '{text:^10}'")

# Number formatting with padding
number = 42
print(f"Number with padding: {number:05d}")

# 5. Print Options
print("\n=== Print Options ===")

# Print with separator
print("Apple", "Banana", "Cherry", sep=", ")

# Print with end character
print("This line ends with a space", end=" ")
print("and this continues on the same line")

# Print multiple lines
print("Line 1\nLine 2\nLine 3")

# 6. File Input/Output Basics
print("\n=== File Input/Output ===")

# Writing to a file
filename = "sample.txt"
with open(filename, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python is awesome!\n")

print(f"Content written to {filename}")

# Reading from a file
with open(filename, "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Reading line by line
print("Reading line by line:")
with open(filename, "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

# 7. Interactive Program Example
print("\n=== Interactive Program ===")

def interactive_calculator():
    print("Welcome to the Interactive Calculator!")
    print("Enter 'quit' to exit")
    
    while True:
        try:
            # Get operation
            operation = input("\nEnter operation (+, -, *, /) or 'quit': ")
            if operation.lower() == 'quit':
                print("Goodbye!")
                break
            
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation! Please use +, -, *, or /")
                continue
            
            # Get numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

# Uncomment the line below to run the interactive calculator
# interactive_calculator()

# 8. Input Validation Examples
print("\n=== Input Validation ===")

def get_positive_number():
    while True:
        try:
            number = float(input("Enter a positive number: "))
            if number > 0:
                return number
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

def get_yes_no():
    while True:
        response = input("Do you want to continue? (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")

# 9. Reading Multiple Values
print("\n=== Reading Multiple Values ===")

# Reading multiple values in one line
values = input("Enter three numbers separated by spaces: ").split()
numbers = [float(x) for x in values]
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")

# Reading comma-separated values
csv_input = input("Enter values separated by commas: ")
csv_values = [x.strip() for x in csv_input.split(',')]
print(f"CSV values: {csv_values}")

# 10. Password Input (hidden)
print("\n=== Password Input ===")

import getpass

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    # Simple validation (in real apps, use proper authentication)
    if username == "admin" and password == "password123":
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False

# Uncomment to test login
# login()

# Exercises:
"""
1. Create a program that asks for user's name, age, and city, then displays a greeting
2. Write a program that calculates the area of a rectangle (length × width)
3. Create a simple quiz program with 3 questions
4. Write a program that reads a file and counts the number of lines
5. Create a program that asks for a number and prints its multiplication table
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. User information program
print("Exercise 1: User Information")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_city = input("Enter your city: ")
print(f"Hello {user_name}! You are {user_age} years old and live in {user_city}.")

# 2. Rectangle area calculator
print("\nExercise 2: Rectangle Area")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"Area of rectangle: {area}")

# 3. Simple quiz
print("\nExercise 3: Simple Quiz")
score = 0

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the largest planet?", "Jupiter")
]

for question, answer in questions:
    user_answer = input(f"{question} ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {answer}")

print(f"Your score: {score}/{len(questions)}")

# 4. File line counter
print("\nExercise 4: File Line Counter")
filename = "sample.txt"
try:
    with open(filename, "r") as file:
        lines = file.readlines()
        print(f"Number of lines in {filename}: {len(lines)}")
except FileNotFoundError:
    print(f"File {filename} not found!")

# 5. Multiplication table
print("\nExercise 5: Multiplication Table")
number = int(input("Enter a number: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

print("\n🎉 Congratulations! You've completed Lesson 3!")
print("Next: Lesson 4 - Operators")
