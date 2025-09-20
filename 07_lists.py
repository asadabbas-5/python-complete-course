# Lesson 7: Lists

"""
This lesson covers:
- Creating and accessing lists
- List methods and operations
- List slicing and indexing
- List comprehensions
- Nested lists
- Common list patterns
- Performance considerations
"""

# 1. Creating Lists
print("=== Creating Lists ===")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# Using list() constructor
list_from_range = list(range(5))
list_from_string = list("Python")

print(f"From range: {list_from_range}")
print(f"From string: {list_from_string}")

# 2. Accessing List Elements
print("\n=== Accessing List Elements ===")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0-based)
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Last fruit: {fruits[4]}")

# Negative indexing
print(f"Last fruit (negative): {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

# 3. List Slicing
print("\n=== List Slicing ===")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Basic slicing [start:end]
print(f"First 3 elements: {numbers[0:3]}")
print(f"Elements 2-5: {numbers[2:6]}")
print(f"Last 3 elements: {numbers[-3:]}")

# Slicing with step [start:end:step]
print(f"Every 2nd element: {numbers[::2]}")
print(f"Reverse list: {numbers[::-1]}")
print(f"Every 3rd element: {numbers[::3]}")

# 4. Modifying Lists
print("\n=== Modifying Lists ===")

# Changing elements
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(f"Modified fruits: {fruits}")

# Adding elements
fruits.append("date")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "apricot")  # Insert at specific position
print(f"After insert: {fruits}")

fruits.extend(["elderberry", "fig"])  # Add multiple elements
print(f"After extend: {fruits}")

# Removing elements
fruits.remove("cherry")  # Remove first occurrence
print(f"After remove: {fruits}")

popped = fruits.pop()  # Remove and return last element
print(f"Popped: {popped}, Remaining: {fruits}")

popped_at_index = fruits.pop(1)  # Remove and return element at index
print(f"Popped at index 1: {popped_at_index}, Remaining: {fruits}")

# 5. List Methods
print("\n=== List Methods ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Information methods
print(f"Length: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

# Sorting
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"Sorted: {numbers_copy}")

numbers_copy.sort(reverse=True)
print(f"Reverse sorted: {numbers_copy}")

# Reversing
numbers_copy.reverse()
print(f"Reversed: {numbers_copy}")

# 6. List Operations
print("\n=== List Operations ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Concatenated: {combined}")

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")

# Membership testing
print(f"Is 2 in list1? {2 in list1}")
print(f"Is 7 in list1? {7 in list1}")

# 7. List Comprehensions
print("\n=== List Comprehensions ===")

# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Multiple variables
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"Coordinates: {coordinates}")

# String manipulation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Upper words: {upper_words}")

# 8. Nested Lists
print("\n=== Nested Lists ===")

# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Accessing elements
print(f"Element at [1][2]: {matrix[1][2]}")
print(f"First row: {matrix[0]}")
print(f"First column: {[row[0] for row in matrix]}")

# 3D list
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print(f"3D list element [0][1][0]: {cube[0][1][0]}")

# 9. Common List Patterns
print("\n=== Common List Patterns ===")

# Pattern 1: Finding maximum and minimum
numbers = [3, 7, 2, 9, 1, 5]
max_num = max(numbers)
min_num = min(numbers)
print(f"Numbers: {numbers}")
print(f"Max: {max_num}, Min: {min_num}")

# Pattern 2: Sum and average
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}, Average: {average:.2f}")

# Pattern 3: Filtering
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Pattern 4: Mapping (transforming)
doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")

# Pattern 5: Finding duplicates
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers_with_duplicates))
print(f"Original: {numbers_with_duplicates}")
print(f"Unique: {unique_numbers}")

# 10. List vs Other Data Structures
print("\n=== List vs Other Data Structures ===")

# Lists are mutable (can be changed)
mutable_list = [1, 2, 3]
mutable_list[0] = 10
print(f"Mutable list: {mutable_list}")

# Lists can contain duplicates
duplicates = [1, 1, 2, 2, 3]
print(f"List with duplicates: {duplicates}")

# Lists maintain order
ordered = [3, 1, 4, 1, 5]
print(f"Ordered list: {ordered}")

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Student grades
def calculate_grades():
    students = ["Alice", "Bob", "Charlie", "Diana"]
    grades = [85, 92, 78, 96]
    
    # Find highest grade
    max_grade = max(grades)
    max_index = grades.index(max_grade)
    top_student = students[max_index]
    
    print(f"Top student: {top_student} with grade {max_grade}")
    
    # Calculate average
    average = sum(grades) / len(grades)
    print(f"Class average: {average:.2f}")
    
    # Students above average
    above_average = [students[i] for i in range(len(students)) if grades[i] > average]
    print(f"Students above average: {above_average}")

calculate_grades()

# Example 2: Shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.prices = []
    
    def add_item(self, item, price):
        self.items.append(item)
        self.prices.append(price)
        print(f"Added {item} for ${price}")
    
    def remove_item(self, item):
        if item in self.items:
            index = self.items.index(item)
            self.items.pop(index)
            price = self.prices.pop(index)
            print(f"Removed {item} (${price})")
        else:
            print(f"{item} not found in cart")
    
    def get_total(self):
        return sum(self.prices)
    
    def display_cart(self):
        print("\nShopping Cart:")
        for i, (item, price) in enumerate(zip(self.items, self.prices), 1):
            print(f"{i}. {item}: ${price}")
        print(f"Total: ${self.get_total()}")

# Test shopping cart
cart = ShoppingCart()
cart.add_item("Apple", 1.50)
cart.add_item("Banana", 0.75)
cart.add_item("Orange", 2.00)
cart.display_cart()
cart.remove_item("Banana")
cart.display_cart()

# Example 3: Matrix operations
def matrix_multiply(a, b):
    """Multiply two 2x2 matrices"""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result_matrix = matrix_multiply(matrix_a, matrix_b)
print(f"Matrix A: {matrix_a}")
print(f"Matrix B: {matrix_b}")
print(f"Result: {result_matrix}")

# 12. Performance Tips
print("\n=== Performance Tips ===")

# Tip 1: Use appropriate methods
# append() is O(1), insert() is O(n)
large_list = list(range(1000))

# Good: append to end
large_list.append(1000)

# Avoid: insert at beginning (slow for large lists)
# large_list.insert(0, -1)  # This is O(n)

# Tip 2: Use list comprehensions for simple transformations
# Instead of:
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x * 2)

# Use:
result = [x * 2 for x in range(10) if x % 2 == 0]

# Tip 3: Use built-in functions
numbers = [1, 2, 3, 4, 5]
# Instead of manual loops, use:
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Exercises:
"""
1. Create a list of your favorite foods and print each one
2. Write a function that finds the second largest number in a list
3. Create a program that removes all duplicates from a list
4. Write a function that rotates a list by n positions
5. Create a program that finds common elements between two lists
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Favorite foods
print("Exercise 1: Favorite Foods")
favorite_foods = ["Pizza", "Pasta", "Ice Cream", "Chocolate", "Sushi"]
for food in favorite_foods:
    print(f"I love {food}!")

# 2. Second largest number
print("\nExercise 2: Second Largest Number")
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[1]

numbers = [3, 7, 2, 9, 1, 5]
second_large = second_largest(numbers)
print(f"Numbers: {numbers}")
print(f"Second largest: {second_large}")

# 3. Remove duplicates
print("\nExercise 3: Remove Duplicates")
def remove_duplicates(lst):
    return list(set(lst))

numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = remove_duplicates(numbers_with_duplicates)
print(f"Original: {numbers_with_duplicates}")
print(f"Unique: {unique_numbers}")

# 4. Rotate list
print("\nExercise 4: Rotate List")
def rotate_list(lst, n):
    n = n % len(lst)  # Handle negative and large values
    return lst[-n:] + lst[:-n]

original = [1, 2, 3, 4, 5]
rotated = rotate_list(original, 2)
print(f"Original: {original}")
print(f"Rotated by 2: {rotated}")

# 5. Common elements
print("\nExercise 5: Common Elements")
def find_common(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = find_common(list1, list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements: {common}")

print("\n🎉 Congratulations! You've completed Lesson 7!")
print("Next: Lesson 8 - Tuples and Sets")
