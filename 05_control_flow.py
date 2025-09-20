# Lesson 5: Control Flow

"""
This lesson covers:
- if, elif, else statements
- Nested conditions
- Ternary operators
- Conditional expressions
- Boolean logic in conditions
- Common patterns and best practices
"""

# 1. Basic if Statement
print("=== Basic if Statement ===")

age = 18
if age >= 18:
    print("You are an adult")

# 2. if-else Statement
print("\n=== if-else Statement ===")

temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not hot outside")

# 3. if-elif-else Statement
print("\n=== if-elif-else Statement ===")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# 4. Multiple Conditions
print("\n=== Multiple Conditions ===")

age = 25
has_license = True
has_car = False

# Using and
if age >= 18 and has_license:
    print("You can drive")

# Using or
if has_car or has_license:
    print("You have transportation options")

# Using not
if not has_car:
    print("You don't have a car")

# Complex conditions
if age >= 18 and has_license and not has_car:
    print("You can drive but need to rent a car")

# 5. Nested Conditions
print("\n=== Nested Conditions ===")

weather = "sunny"
temperature = 28
wind_speed = 5

if weather == "sunny":
    if temperature > 25:
        if wind_speed < 10:
            print("Perfect day for the beach!")
        else:
            print("Too windy for the beach")
    else:
        print("Nice day but not hot enough for beach")
else:
    print("Not a beach day")

# 6. Ternary Operator (Conditional Expression)
print("\n=== Ternary Operator ===")

age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Multiple ternary operators
score = 75
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Grade: {grade}")

# 7. Truthiness and Falsiness
print("\n=== Truthiness and Falsiness ===")

# Falsy values: False, None, 0, 0.0, "", [], {}, set()
# Truthy values: Everything else

values = [True, False, 1, 0, "hello", "", [1, 2], [], {"a": 1}, {}, None]

for value in values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

# 8. Short-circuit Evaluation
print("\n=== Short-circuit Evaluation ===")

def expensive_operation():
    print("This is expensive!")
    return True

# Short-circuit AND - second condition won't be evaluated if first is False
result1 = False and expensive_operation()
print(f"False and expensive_operation(): {result1}")

# Short-circuit OR - second condition won't be evaluated if first is True
result2 = True or expensive_operation()
print(f"True or expensive_operation(): {result2}")

# 9. Common Patterns
print("\n=== Common Patterns ===")

# Pattern 1: Checking for valid input
user_input = "hello"
if user_input and user_input.strip():
    print("Valid input received")
else:
    print("Invalid or empty input")

# Pattern 2: Default values
name = None
display_name = name if name else "Guest"
print(f"Welcome, {display_name}!")

# Pattern 3: Range checking
number = 15
if 10 <= number <= 20:
    print(f"{number} is between 10 and 20")

# Pattern 4: Multiple value checking
day = "Monday"
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a weekday")
elif day in ["Saturday", "Sunday"]:
    print("It's a weekend")
else:
    print("Invalid day")

# 10. Error Handling with Conditions
print("\n=== Error Handling with Conditions ===")

def safe_divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Invalid input types"
    else:
        return a / b

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")

# 11. Complex Decision Making
print("\n=== Complex Decision Making ===")

def determine_shipping_cost(weight, distance, is_express=False):
    base_cost = 5.00
    
    # Weight-based pricing
    if weight <= 1:
        weight_cost = 0
    elif weight <= 5:
        weight_cost = 2.00
    elif weight <= 10:
        weight_cost = 5.00
    else:
        weight_cost = 10.00
    
    # Distance-based pricing
    if distance <= 50:
        distance_cost = 0
    elif distance <= 100:
        distance_cost = 3.00
    else:
        distance_cost = 6.00
    
    # Express shipping
    express_multiplier = 2.0 if is_express else 1.0
    
    total_cost = (base_cost + weight_cost + distance_cost) * express_multiplier
    return total_cost

# Test shipping calculator
print(f"Shipping cost (2kg, 75km, regular): ${determine_shipping_cost(2, 75):.2f}")
print(f"Shipping cost (2kg, 75km, express): ${determine_shipping_cost(2, 75, True):.2f}")
print(f"Shipping cost (8kg, 150km, regular): ${determine_shipping_cost(8, 150):.2f}")

# 12. Menu System Example
print("\n=== Menu System Example ===")

def show_menu():
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def calculator_menu():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    result = num1 + num2
                    operation = "addition"
                elif choice == "2":
                    result = num1 - num2
                    operation = "subtraction"
                elif choice == "3":
                    result = num1 * num2
                    operation = "multiplication"
                elif choice == "4":
                    if num2 == 0:
                        print("Error: Division by zero!")
                        continue
                    result = num1 / num2
                    operation = "division"
                
                print(f"Result of {operation}: {result}")
                
            except ValueError:
                print("Error: Please enter valid numbers!")
        else:
            print("Invalid choice! Please enter 1-5.")

# Uncomment to run the calculator menu
# calculator_menu()

# 13. Best Practices
print("\n=== Best Practices ===")

# Good: Clear and readable conditions
def is_valid_email(email):
    return email and "@" in email and "." in email.split("@")[-1]

# Good: Use meaningful variable names
is_weekend = True
has_work = False

if is_weekend and not has_work:
    print("Time to relax!")

# Good: Avoid deep nesting
def process_user(user):
    if not user:
        return "No user provided"
    
    if not user.get("name"):
        return "User name required"
    
    if not user.get("email"):
        return "User email required"
    
    return "User processed successfully"

# Good: Use early returns
def calculate_discount(price, user_type):
    if price <= 0:
        return 0
    
    if user_type == "premium":
        return price * 0.2
    elif user_type == "regular":
        return price * 0.1
    else:
        return 0

# Exercises:
"""
1. Write a program that determines if a number is positive, negative, or zero
2. Create a simple grade calculator that assigns letter grades based on percentage
3. Write a program that checks if a year is a leap year
4. Create a program that determines the type of triangle based on side lengths
5. Write a program that converts temperature between Celsius and Fahrenheit
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Number classification
print("Exercise 1: Number Classification")
number = -5
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

# 2. Grade calculator
print("\nExercise 2: Grade Calculator")
percentage = 87
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Percentage: {percentage}%, Grade: {grade}")

# 3. Leap year checker
print("\nExercise 3: Leap Year")
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 4. Triangle type
print("\nExercise 4: Triangle Type")
a, b, c = 3, 4, 5
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        triangle_type = "equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    print(f"Triangle with sides {a}, {b}, {c} is {triangle_type}")
else:
    print("Not a valid triangle")

# 5. Temperature converter
print("\nExercise 5: Temperature Converter")
temp = 25
unit = "C"  # C for Celsius, F for Fahrenheit

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit}°F")
elif unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F = {celsius}°C")
else:
    print("Invalid unit")

print("\n🎉 Congratulations! You've completed Lesson 5!")
print("Next: Lesson 6 - Loops")
