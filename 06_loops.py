# Lesson 6: Loops

"""
This lesson covers:
- for loops
- while loops
- Loop control (break, continue, pass)
- Nested loops
- Loop with else clause
- Common loop patterns
- Performance considerations
"""

# 1. for Loop Basics
print("=== for Loop Basics ===")

# Iterating over a range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("\nFruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Iterating over a string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(letter)

# 2. range() Function
print("\n=== range() Function ===")

print("range(5):", list(range(5)))
print("range(1, 6):", list(range(1, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))

# Using range with for loop
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# 3. while Loop Basics
print("\n=== while Loop Basics ===")

# Basic while loop
count = 0
print("Counting with while loop:")
while count < 5:
    print(f"Count: {count}")
    count += 1

# while loop with user input
print("\nWhile loop with condition:")
number = 1
while number <= 10:
    print(f"Number: {number}")
    number += 2

# 4. Loop Control Statements
print("\n=== Loop Control Statements ===")

# break statement
print("Using break:")
for i in range(10):
    if i == 5:
        break
    print(f"i = {i}")

# continue statement
print("\nUsing continue (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"i = {i}")

# pass statement
print("\nUsing pass:")
for i in range(5):
    if i == 2:
        pass  # Do nothing
    else:
        print(f"i = {i}")

# 5. Nested Loops
print("\n=== Nested Loops ===")

# Multiplication table
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()  # Empty line after each row

# Pattern printing
print("Star pattern:")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# 6. Loop with else Clause
print("\n=== Loop with else Clause ===")

# for loop with else
print("Searching for number 3:")
for i in range(5):
    if i == 3:
        print(f"Found {i}!")
        break
else:
    print("Number 3 not found")

print("Searching for number 7:")
for i in range(5):
    if i == 7:
        print(f"Found {i}!")
        break
else:
    print("Number 7 not found")

# while loop with else
print("\nWhile loop with else:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed normally")

# 7. enumerate() Function
print("\n=== enumerate() Function ===")

fruits = ["apple", "banana", "cherry"]
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Starting from different number
print("\nFruits with custom index:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 8. zip() Function
print("\n=== zip() Function ===")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("Combined information:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# 9. Common Loop Patterns
print("\n=== Common Loop Patterns ===")

# Pattern 1: Summing numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers}: {total}")

# Pattern 2: Finding maximum
numbers = [3, 7, 2, 9, 1]
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
print(f"Maximum in {numbers}: {max_num}")

# Pattern 3: Counting occurrences
text = "hello world"
letter_count = {}
for letter in text:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(f"Letter count in '{text}': {letter_count}")

# Pattern 4: Building lists
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares: {squares}")

# 10. List Comprehensions (Preview)
print("\n=== List Comprehensions (Preview) ===")

# Traditional loop
squares_loop = []
for i in range(1, 6):
    squares_loop.append(i ** 2)

# List comprehension
squares_comp = [i ** 2 for i in range(1, 6)]

print(f"Squares (loop): {squares_loop}")
print(f"Squares (comprehension): {squares_comp}")

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Number guessing game
def number_guessing_game():
    import random
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3
    
    print("Guess a number between 1 and 10!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
                
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The number was {secret_number}")

# Uncomment to play the game
# number_guessing_game()

# Example 2: Password validation
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    if not has_digit:
        return False, "Password must contain at least one digit"
    
    return True, "Password is valid"

# Test password validation
test_passwords = ["weak", "Strong123", "password", "MyPassword123"]
for pwd in test_passwords:
    is_valid, message = validate_password(pwd)
    print(f"'{pwd}': {message}")

# Example 3: Menu system with loops
def menu_system():
    while True:
        print("\n=== Menu ===")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("You selected Option 1")
        elif choice == "2":
            print("You selected Option 2")
        elif choice == "3":
            print("You selected Option 3")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Uncomment to run menu system
# menu_system()

# 12. Performance Tips
print("\n=== Performance Tips ===")

# Tip 1: Use appropriate loop type
# Use for loop when you know the number of iterations
# Use while loop when you need to check a condition

# Tip 2: Avoid unnecessary computations inside loops
# Bad: expensive_operation() called every iteration
# Good: compute once outside the loop

# Tip 3: Use built-in functions when possible
numbers = [1, 2, 3, 4, 5]

# Instead of manual loop
total = 0
for num in numbers:
    total += num

# Use built-in sum()
total_builtin = sum(numbers)
print(f"Sum: {total} vs {total_builtin}")

# Exercises:
"""
1. Write a program that prints all even numbers from 1 to 20
2. Create a program that calculates the factorial of a number
3. Write a program that finds the sum of all numbers divisible by 3 or 5 up to 100
4. Create a program that prints a triangle pattern using loops
5. Write a program that simulates a simple ATM with withdrawal limits
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Even numbers
print("Exercise 1: Even numbers from 1 to 20")
for i in range(2, 21, 2):
    print(i)

# 2. Factorial
print("\nExercise 2: Factorial")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n}: {factorial}")

# 3. Sum of numbers divisible by 3 or 5
print("\nExercise 3: Sum of numbers divisible by 3 or 5")
total = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(f"Sum of numbers divisible by 3 or 5 up to 100: {total}")

# 4. Triangle pattern
print("\nExercise 4: Triangle pattern")
for i in range(1, 6):
    print("*" * i)

# 5. Simple ATM simulation
print("\nExercise 5: Simple ATM")
balance = 1000
max_withdrawal = 500

while True:
    print(f"\nCurrent balance: ${balance}")
    print("1. Withdraw")
    print("2. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds!")
        elif amount > max_withdrawal:
            print(f"Maximum withdrawal is ${max_withdrawal}")
        else:
            balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${balance}")
    elif choice == "2":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

print("\n🎉 Congratulations! You've completed Lesson 6!")
print("Next: Lesson 7 - Lists")
