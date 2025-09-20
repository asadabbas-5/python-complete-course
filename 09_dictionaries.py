# Lesson 9: Dictionaries

"""
This lesson covers:
- Creating and accessing dictionaries
- Dictionary methods and operations
- Dictionary comprehensions
- Nested dictionaries
- Dictionary vs other data structures
- Common patterns and best practices
"""

# 1. Creating Dictionaries
print("=== Creating Dictionaries ===")

# Empty dictionary
empty_dict = {}
empty_dict_constructor = dict()

# Dictionary with values
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="London")

# Dictionary with mixed data types
mixed_dict = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "nested": {"key": "value"}
}

print(f"Empty dict: {empty_dict}")
print(f"Person: {person}")
print(f"Person2: {person2}")
print(f"Mixed dict: {mixed_dict}")

# 2. Accessing Dictionary Elements
print("\n=== Accessing Dictionary Elements ===")

student = {
    "name": "Charlie",
    "age": 22,
    "grades": [85, 90, 78, 92],
    "is_active": True
}

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grades: {student['grades']}")

# Using get() method (safer)
print(f"Name (get): {student.get('name')}")
print(f"Phone (get): {student.get('phone', 'Not provided')}")

# Accessing nested values
print(f"First grade: {student['grades'][0]}")

# 3. Modifying Dictionaries
print("\n=== Modifying Dictionaries ===")

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
print(f"Original inventory: {inventory}")

# Adding new items
inventory["grapes"] = 15
print(f"After adding grapes: {inventory}")

# Updating existing items
inventory["apples"] = 12
print(f"After updating apples: {inventory}")

# Updating multiple items
inventory.update({"bananas": 7, "cherries": 3})
print(f"After bulk update: {inventory}")

# Removing items
del inventory["oranges"]
print(f"After deleting oranges: {inventory}")

removed_value = inventory.pop("bananas")
print(f"Removed bananas: {removed_value}")
print(f"After pop: {inventory}")

# 4. Dictionary Methods
print("\n=== Dictionary Methods ===")

scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 88}

# keys() - get all keys
print(f"Keys: {list(scores.keys())}")

# values() - get all values
print(f"Values: {list(scores.values())}")

# items() - get key-value pairs
print(f"Items: {list(scores.items())}")

# Iterating over dictionary
print("Iterating over dictionary:")
for name, score in scores.items():
    print(f"{name}: {score}")

# 5. Dictionary Comprehensions
print("\n=== Dictionary Comprehensions ===")

# Basic dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age_dict = {name: age for name, age in zip(names, ages)}
print(f"Name-age dict: {name_age_dict}")

# String manipulation
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# 6. Nested Dictionaries
print("\n=== Nested Dictionaries ===")

# Simple nested dictionary
company = {
    "name": "TechCorp",
    "employees": {
        "Alice": {
            "position": "Developer",
            "salary": 75000,
            "department": "Engineering"
        },
        "Bob": {
            "position": "Manager",
            "salary": 90000,
            "department": "Engineering"
        }
    },
    "departments": {
        "Engineering": {"budget": 500000, "head": "Bob"},
        "Marketing": {"budget": 200000, "head": "Carol"}
    }
}

print(f"Company: {company['name']}")
print(f"Alice's position: {company['employees']['Alice']['position']}")
print(f"Engineering budget: {company['departments']['Engineering']['budget']}")

# Accessing nested values safely
alice_salary = company.get("employees", {}).get("Alice", {}).get("salary", "Not found")
print(f"Alice's salary: {alice_salary}")

# 7. Dictionary Operations
print("\n=== Dictionary Operations ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merging dictionaries (Python 3.9+)
merged = dict1 | dict2
print(f"Merged dict: {merged}")

# Using update()
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"Updated dict: {dict1_copy}")

# Checking membership
print(f"'a' in dict1: {'a' in dict1}")
print(f"'d' in dict1: {'d' in dict1}")

# Length
print(f"Length of dict1: {len(dict1)}")

# 8. Common Dictionary Patterns
print("\n=== Common Dictionary Patterns ===")

# Pattern 1: Counting occurrences
text = "hello world hello python world"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"Word count: {word_count}")

# Pattern 2: Grouping
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"}
]

# Group by grade
grade_groups = {}
for student in students:
    grade = student["grade"]
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append(student["name"])

print(f"Grade groups: {grade_groups}")

# Pattern 3: Default values
config = {
    "host": "localhost",
    "port": 8080
}

# Set defaults
config.setdefault("debug", False)
config.setdefault("timeout", 30)
print(f"Config with defaults: {config}")

# 9. Dictionary vs Other Data Structures
print("\n=== Dictionary vs Other Data Structures ===")

# Dictionary: Key-value pairs, fast lookup
user_info = {"name": "Alice", "email": "alice@example.com", "age": 25}

# List: Ordered, indexed by position
user_list = ["Alice", "alice@example.com", 25]

# Tuple: Immutable, ordered
user_tuple = ("Alice", "alice@example.com", 25)

print(f"Dictionary access: {user_info['name']}")
print(f"List access: {user_list[0]}")
print(f"Tuple access: {user_tuple[0]}")

# Dictionary advantages:
# - Meaningful keys
# - Fast O(1) lookup
# - Easy to modify
# - Can store different data types

# 10. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Student Grade Book
class GradeBook:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name):
        self.students[name] = []
    
    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
        else:
            print(f"Student {name} not found")
    
    def get_average(self, name):
        if name in self.students and self.students[name]:
            return sum(self.students[name]) / len(self.students[name])
        return None
    
    def get_all_averages(self):
        averages = {}
        for name, grades in self.students.items():
            if grades:
                averages[name] = sum(grades) / len(grades)
        return averages

# Test grade book
gradebook = GradeBook()
gradebook.add_student("Alice")
gradebook.add_student("Bob")

gradebook.add_grade("Alice", 85)
gradebook.add_grade("Alice", 90)
gradebook.add_grade("Bob", 78)
gradebook.add_grade("Bob", 92)

print(f"Alice's average: {gradebook.get_average('Alice')}")
print(f"All averages: {gradebook.get_all_averages()}")

# Example 2: Configuration Management
class Config:
    def __init__(self, config_dict=None):
        self.config = config_dict or {}
        self.defaults = {
            "debug": False,
            "port": 8080,
            "host": "localhost",
            "timeout": 30
        }
    
    def get(self, key, default=None):
        return self.config.get(key, self.defaults.get(key, default))
    
    def set(self, key, value):
        self.config[key] = value
    
    def update(self, new_config):
        self.config.update(new_config)

# Test configuration
config = Config({"port": 3000, "debug": True})
print(f"Port: {config.get('port')}")
print(f"Host: {config.get('host')}")
print(f"Debug: {config.get('debug')}")

# Example 3: Cache Implementation
class SimpleCache:
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size
        self.access_order = []
    
    def get(self, key):
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def set(self, key, value):
        if len(self.cache) >= self.max_size and key not in self.cache:
            # Remove least recently used
            oldest_key = self.access_order.pop(0)
            del self.cache[oldest_key]
        
        self.cache[key] = value
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)

# Test cache
cache = SimpleCache(max_size=3)
cache.set("a", 1)
cache.set("b", 2)
cache.set("c", 3)
print(f"Cache after adding a,b,c: {cache.cache}")

cache.get("a")  # Access 'a' to make it recently used
cache.set("d", 4)  # This should remove 'b' (least recently used)
print(f"Cache after adding d: {cache.cache}")

# 11. Advanced Dictionary Techniques
print("\n=== Advanced Dictionary Techniques ===")

# defaultdict - automatic default values
from collections import defaultdict

# Grouping with defaultdict
words = ["apple", "banana", "cherry", "apricot", "blueberry"]
grouped_by_length = defaultdict(list)

for word in words:
    grouped_by_length[len(word)].append(word)

print(f"Grouped by length: {dict(grouped_by_length)}")

# Counter - counting occurrences
from collections import Counter

text = "hello world hello python"
word_counter = Counter(text.split())
print(f"Word counter: {word_counter}")
print(f"Most common: {word_counter.most_common(2)}")

# ChainMap - combining multiple dictionaries
from collections import ChainMap

default_config = {"debug": False, "port": 8080}
user_config = {"port": 3000, "host": "localhost"}
env_config = {"debug": True}

combined_config = ChainMap(env_config, user_config, default_config)
print(f"Combined config: {dict(combined_config)}")

# 12. Performance Tips
print("\n=== Performance Tips ===")

# Tip 1: Use appropriate data structures
# Dictionary lookup is O(1), list lookup is O(n)

# Tip 2: Use dict.get() for safe access
# Instead of: value = my_dict['key']  # KeyError if missing
# Use: value = my_dict.get('key', default_value)

# Tip 3: Use dictionary comprehensions for simple transformations
# Instead of loops, use comprehensions when possible

# Tip 4: Consider using defaultdict for grouping operations
# It automatically creates missing keys

# Exercises:
"""
1. Create a dictionary of your favorite foods and their prices
2. Write a function that counts the frequency of each character in a string
3. Create a program that stores student information (name, age, grades)
4. Write a function that finds the most common word in a text
5. Create a simple phone book with add, search, and delete functions
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Favorite foods dictionary
print("Exercise 1: Favorite Foods")
favorite_foods = {
    "Pizza": 15.99,
    "Pasta": 12.50,
    "Ice Cream": 4.99,
    "Chocolate": 3.50,
    "Sushi": 18.00
}

for food, price in favorite_foods.items():
    print(f"{food}: ${price}")

# 2. Character frequency counter
print("\nExercise 2: Character Frequency")
def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():  # Only count letters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

text = "Hello World"
char_freq = count_characters(text)
print(f"Character frequency in '{text}': {char_freq}")

# 3. Student information storage
print("\nExercise 3: Student Information")
students = {
    "Alice": {"age": 20, "grades": [85, 90, 78]},
    "Bob": {"age": 22, "grades": [92, 88, 95]},
    "Charlie": {"age": 21, "grades": [76, 82, 80]}
}

for name, info in students.items():
    avg_grade = sum(info["grades"]) / len(info["grades"])
    print(f"{name}: Age {info['age']}, Average Grade {avg_grade:.1f}")

# 4. Most common word
print("\nExercise 4: Most Common Word")
def most_common_word(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    if word_count:
        return max(word_count, key=word_count.get)
    return None

text = "python is great python is awesome python is powerful"
most_common = most_common_word(text)
print(f"Most common word in '{text}': {most_common}")

# 5. Simple phone book
print("\nExercise 5: Phone Book")
class PhoneBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Added {name}: {phone}")
    
    def search_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        return None
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted {name}")
        else:
            print(f"{name} not found")
    
    def list_contacts(self):
        print("Phone Book:")
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}")

# Test phone book
phonebook = PhoneBook()
phonebook.add_contact("Alice", "123-456-7890")
phonebook.add_contact("Bob", "098-765-4321")
phonebook.list_contacts()

search_result = phonebook.search_contact("Alice")
print(f"Alice's number: {search_result}")

phonebook.delete_contact("Bob")
phonebook.list_contacts()

print("\n🎉 Congratulations! You've completed Lesson 9!")
print("Next: Lesson 10 - String Methods")
