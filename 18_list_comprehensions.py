# Lesson 18: List Comprehensions

"""
This lesson covers:
- Basic list comprehensions
- Conditional list comprehensions
- Nested list comprehensions
- Dictionary and set comprehensions
- Generator expressions
- Performance considerations
- Best practices and common patterns
"""

# 1. Basic List Comprehensions
print("=== Basic List Comprehensions ===")

# Traditional approach
squares_traditional = []
for i in range(1, 6):
    squares_traditional.append(i ** 2)

# List comprehension approach
squares_comprehension = [i ** 2 for i in range(1, 6)]

print(f"Traditional: {squares_traditional}")
print(f"Comprehension: {squares_comprehension}")

# More examples
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Upper words: {upper_words}")

# 2. Conditional List Comprehensions
print("\n=== Conditional List Comprehensions ===")

# Filter even numbers
numbers = list(range(1, 11))
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Filter words by length
words = ["python", "java", "c", "javascript", "go", "rust"]
long_words = [word for word in words if len(word) > 3]
print(f"Long words: {long_words}")

# Multiple conditions
numbers = list(range(1, 21))
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"Divisible by 2 and 3: {filtered}")

# 3. List Comprehensions with Transformations
print("\n=== List Comprehensions with Transformations ===")

# Transform and filter
numbers = list(range(1, 11))
squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Squared evens: {squared_evens}")

# String transformations
sentences = ["hello world", "python programming", "data science"]
word_counts = [len(sentence.split()) for sentence in sentences]
print(f"Word counts: {word_counts}")

# Mathematical operations
temperatures_celsius = [0, 20, 30, 40, 100]
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]
print(f"Fahrenheit: {temperatures_fahrenheit}")

# 4. Nested List Comprehensions
print("\n=== Nested List Comprehensions ===")

# Flatten a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(f"Flattened: {flattened}")

# Create a matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Transpose a matrix
original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in original_matrix] for i in range(len(original_matrix[0]))]
print(f"Transposed: {transposed}")

# 5. Dictionary Comprehensions
print("\n=== Dictionary Comprehensions ===")

# Create a dictionary from lists
keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
my_dict = {k: v for k, v in zip(keys, values)}
print(f"Dictionary: {my_dict}")

# Create a dictionary with conditions
numbers = list(range(1, 11))
squares_dict = {x: x ** 2 for x in numbers if x % 2 == 0}
print(f"Squares dict: {squares_dict}")

# Transform existing dictionary
original_dict = {"apple": 1.5, "banana": 0.8, "orange": 2.0}
discounted_prices = {fruit: price * 0.9 for fruit, price in original_dict.items()}
print(f"Discounted prices: {discounted_prices}")

# 6. Set Comprehensions
print("\n=== Set Comprehensions ===")

# Create a set from a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = {x for x in numbers}
print(f"Unique numbers: {unique_numbers}")

# Create a set with conditions
words = ["hello", "world", "python", "programming", "world", "python"]
long_words_set = {word for word in words if len(word) > 5}
print(f"Long words set: {long_words_set}")

# Mathematical operations on sets
numbers = list(range(1, 21))
squares_set = {x ** 2 for x in numbers if x % 2 == 0}
print(f"Squares set: {squares_set}")

# 7. Generator Expressions
print("\n=== Generator Expressions ===")

# Generator expression (memory efficient)
squares_gen = (x ** 2 for x in range(1, 6))
print(f"Generator: {squares_gen}")
print(f"Generator values: {list(squares_gen)}")

# Generator with conditions
even_squares_gen = (x ** 2 for x in range(1, 11) if x % 2 == 0)
print(f"Even squares: {list(even_squares_gen)}")

# Using generator in functions
def sum_of_squares(n):
    return sum(x ** 2 for x in range(1, n + 1))

print(f"Sum of squares 1-5: {sum_of_squares(5)}")

# 8. Complex List Comprehensions
print("\n=== Complex List Comprehensions ===")

# Multiple variables
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"Coordinates: {coordinates}")

# String processing
text = "hello world python programming"
words = text.split()
word_info = [(word, len(word), word.upper()) for word in words]
print(f"Word info: {word_info}")

# File processing simulation
file_lines = ["line 1", "line 2", "line 3", "error line", "line 5"]
processed_lines = [line.upper() for line in file_lines if not line.startswith("error")]
print(f"Processed lines: {processed_lines}")

# 9. Performance Considerations
print("\n=== Performance Considerations ===")

import time

# Large dataset
large_range = range(1000000)

# List comprehension
start_time = time.time()
squares_list = [x ** 2 for x in large_range]
list_time = time.time() - start_time

# Generator expression
start_time = time.time()
squares_gen = (x ** 2 for x in large_range)
gen_time = time.time() - start_time

print(f"List comprehension time: {list_time:.4f}s")
print(f"Generator expression time: {gen_time:.4f}s")
print(f"Memory usage difference: List uses more memory")

# When to use each
print("\nWhen to use list comprehensions:")
print("- When you need the full result immediately")
print("- When you need to access elements multiple times")
print("- When the dataset is small to medium")

print("\nWhen to use generator expressions:")
print("- When working with large datasets")
print("- When you only need to iterate once")
print("- When memory efficiency is important")

# 10. Common Patterns and Best Practices
print("\n=== Common Patterns and Best Practices ===")

# Pattern 1: Data transformation
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformed = [x * 2 if x % 2 == 0 else x * 3 for x in data]
print(f"Transformed data: {transformed}")

# Pattern 2: Filtering and mapping
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 96}
]
high_achievers = [student["name"] for student in students if student["grade"] >= 90]
print(f"High achievers: {high_achievers}")

# Pattern 3: Nested data processing
nested_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sums = [sum(row) for row in nested_data]
print(f"Row sums: {sums}")

# Pattern 4: String processing
sentences = [
    "Python is awesome",
    "Programming is fun",
    "Data science rocks"
]
word_lists = [sentence.split() for sentence in sentences]
all_words = [word for word_list in word_lists for word in word_list]
print(f"All words: {all_words}")

# Best Practice 1: Keep comprehensions readable
# Good
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

# Bad (too complex)
complex_result = [x ** 2 for x in range(1, 11) if x % 2 == 0 and x > 2 and x < 8 and x != 6]

# Best Practice 2: Use appropriate data structures
# For unique values, use set comprehension
unique_words = {word.lower() for word in ["Hello", "WORLD", "hello", "Python"]}
print(f"Unique words: {unique_words}")

# For key-value pairs, use dict comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(f"Word lengths: {word_lengths}")

# 11. Advanced Examples
print("\n=== Advanced Examples ===")

# Example 1: Data Analysis
sales_data = [
    {"product": "laptop", "price": 1000, "quantity": 2},
    {"product": "mouse", "price": 25, "quantity": 10},
    {"product": "keyboard", "price": 75, "quantity": 5},
    {"product": "monitor", "price": 300, "quantity": 3}
]

# Calculate total revenue per product
revenue = {item["product"]: item["price"] * item["quantity"] for item in sales_data}
print(f"Revenue: {revenue}")

# Find expensive products
expensive_products = [item["product"] for item in sales_data if item["price"] > 100]
print(f"Expensive products: {expensive_products}")

# Example 2: Text Processing
text = "Python is a great programming language. Python is versatile and powerful."
words = text.lower().replace(".", "").split()

# Word frequency
word_freq = {word: words.count(word) for word in set(words)}
print(f"Word frequency: {word_freq}")

# Long words
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")

# Example 3: Matrix Operations
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Matrix addition
matrix_sum = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] 
              for i in range(len(matrix_a))]
print(f"Matrix sum: {matrix_sum}")

# Example 4: File Processing Simulation
file_contents = [
    "import os",
    "import sys",
    "def main():",
    "    print('Hello, World!')",
    "    return 0",
    "if __name__ == '__main__':",
    "    main()"
]

# Extract import statements
imports = [line.strip() for line in file_contents if line.strip().startswith("import")]
print(f"Imports: {imports}")

# Extract function definitions
functions = [line.strip() for line in file_contents if line.strip().startswith("def ")]
print(f"Functions: {functions}")

# 12. Practical Applications
print("\n=== Practical Applications ===")

# Application 1: Data Cleaning
raw_data = ["  apple  ", "banana", "  orange  ", "grape", "  kiwi  "]
cleaned_data = [item.strip() for item in raw_data]
print(f"Cleaned data: {cleaned_data}")

# Application 2: Configuration Processing
config_lines = [
    "debug=true",
    "port=8080",
    "host=localhost",
    "timeout=30",
    "invalid_line",
    "database_url=sqlite:///app.db"
]

config_dict = {line.split("=")[0]: line.split("=")[1] 
               for line in config_lines if "=" in line}
print(f"Config: {config_dict}")

# Application 3: Data Validation
user_inputs = ["123", "abc", "456", "def", "789"]
valid_numbers = [int(x) for x in user_inputs if x.isdigit()]
print(f"Valid numbers: {valid_numbers}")

# Application 4: API Response Processing
api_responses = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Charlie", "active": True}
]

active_users = [user["name"] for user in api_responses if user["active"]]
print(f"Active users: {active_users}")

# Exercises:
"""
1. Create a list comprehension that generates squares of even numbers from 1 to 20
2. Write a list comprehension that filters words longer than 5 characters from a list
3. Create a dictionary comprehension that maps numbers to their factorials
4. Write a list comprehension that flattens a nested list
5. Create a set comprehension that finds unique characters in a string
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Squares of even numbers
print("Exercise 1: Squares of Even Numbers")
even_squares = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# 2. Filter long words
print("\nExercise 2: Filter Long Words")
words = ["python", "java", "javascript", "go", "rust", "c++"]
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")

# 3. Number to factorial mapping
print("\nExercise 3: Number to Factorial Mapping")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

numbers = [1, 2, 3, 4, 5]
factorial_dict = {n: factorial(n) for n in numbers}
print(f"Factorial mapping: {factorial_dict}")

# 4. Flatten nested list
print("\nExercise 4: Flatten Nested List")
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(f"Flattened: {flattened}")

# 5. Unique characters
print("\nExercise 5: Unique Characters")
text = "hello world"
unique_chars = {char for char in text if char.isalpha()}
print(f"Unique characters: {unique_chars}")

print("\n🎉 Congratulations! You've completed Lesson 18!")
print("Next: Lesson 19 - DateTime Module")
