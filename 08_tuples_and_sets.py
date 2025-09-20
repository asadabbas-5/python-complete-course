# Lesson 8: Tuples and Sets

"""
This lesson covers:
- Tuples: creation, access, immutability
- Tuple methods and operations
- Sets: creation, methods, operations
- Set operations (union, intersection, difference)
- When to use tuples vs lists vs sets
- Practical applications
"""

# 1. Tuples - Immutable Sequences
print("=== Tuples - Immutable Sequences ===")

# Creating tuples
empty_tuple = ()
single_tuple = (42,)  # Note the comma for single element
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single_tuple}")
print(f"Numbers tuple: {numbers}")
print(f"Mixed tuple: {mixed}")

# Tuple without parentheses (tuple packing)
packed = 1, 2, 3, 4
print(f"Packed tuple: {packed}")

# Tuple unpacking
a, b, c, d = packed
print(f"Unpacked: a={a}, b={b}, c={c}, d={d}")

# 2. Accessing Tuple Elements
print("\n=== Accessing Tuple Elements ===")

coordinates = (10, 20, 30)
print(f"Coordinates: {coordinates}")
print(f"First coordinate: {coordinates[0]}")
print(f"Last coordinate: {coordinates[-1]}")
print(f"Middle coordinate: {coordinates[1]}")

# Tuple slicing
print(f"First two: {coordinates[:2]}")
print(f"Last two: {coordinates[-2:]}")
print(f"Reverse: {coordinates[::-1]}")

# 3. Tuple Methods
print("\n=== Tuple Methods ===")

numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers: {numbers}")

# count() - count occurrences
print(f"Count of 2: {numbers.count(2)}")

# index() - find first occurrence
print(f"Index of 3: {numbers.index(3)}")

# len() - length
print(f"Length: {len(numbers)}")

# 4. Tuple Operations
print("\n=== Tuple Operations ===")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Membership testing
print(f"Is 2 in tuple1? {2 in tuple1}")
print(f"Is 7 in tuple1? {7 in tuple1}")

# 5. Tuple Immutability
print("\n=== Tuple Immutability ===")

immutable_tuple = (1, 2, 3)
print(f"Original: {immutable_tuple}")

# This would cause an error:
# immutable_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# But you can create new tuples
new_tuple = immutable_tuple + (4, 5)
print(f"New tuple: {new_tuple}")

# 6. Sets - Unordered Collections
print("\n=== Sets - Unordered Collections ===")

# Creating sets
empty_set = set()
numbers_set = {1, 2, 3, 4, 5}
string_set = {"apple", "banana", "cherry"}
mixed_set = {1, "hello", 3.14, True}

print(f"Empty set: {empty_set}")
print(f"Numbers set: {numbers_set}")
print(f"String set: {string_set}")
print(f"Mixed set: {mixed_set}")

# Note: Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 3, 3, 4}
print(f"Set with duplicates: {duplicate_set}")

# 7. Set Methods
print("\n=== Set Methods ===")

fruits = {"apple", "banana", "cherry"}
print(f"Original fruits: {fruits}")

# Adding elements
fruits.add("date")
print(f"After add: {fruits}")

fruits.update(["elderberry", "fig"])
print(f"After update: {fruits}")

# Removing elements
fruits.remove("banana")  # Raises KeyError if not found
print(f"After remove: {fruits}")

fruits.discard("grape")  # No error if not found
print(f"After discard: {fruits}")

popped = fruits.pop()  # Removes arbitrary element
print(f"Popped: {popped}, Remaining: {fruits}")

# 8. Set Operations
print("\n=== Set Operations ===")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union
union = set1 | set2
union_method = set1.union(set2)
print(f"Union (|): {union}")
print(f"Union method: {union_method}")

# Intersection
intersection = set1 & set2
intersection_method = set1.intersection(set2)
print(f"Intersection (&): {intersection}")
print(f"Intersection method: {intersection_method}")

# Difference
difference = set1 - set2
difference_method = set1.difference(set2)
print(f"Difference (-): {difference}")
print(f"Difference method: {difference_method}")

# Symmetric difference
symmetric_diff = set1 ^ set2
symmetric_diff_method = set1.symmetric_difference(set2)
print(f"Symmetric difference (^): {symmetric_diff}")
print(f"Symmetric difference method: {symmetric_diff_method}")

# 9. Set Comparisons
print("\n=== Set Comparisons ===")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4}
set_c = {1, 2, 3}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")

# Subset
print(f"Is A subset of B? {set_a.issubset(set_b)}")
print(f"Is A <= B? {set_a <= set_b}")

# Superset
print(f"Is B superset of A? {set_b.issuperset(set_a)}")
print(f"Is B >= A? {set_b >= set_a}")

# Disjoint
print(f"Are A and B disjoint? {set_a.isdisjoint(set_b)}")

# 10. Practical Applications
print("\n=== Practical Applications ===")

# Application 1: Coordinates (tuples)
def calculate_distance(point1, point2):
    """Calculate distance between two 2D points"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

point_a = (0, 0)
point_b = (3, 4)
distance = calculate_distance(point_a, point_b)
print(f"Distance between {point_a} and {point_b}: {distance:.2f}")

# Application 2: Database records (tuples)
students = [
    ("Alice", 25, "Computer Science"),
    ("Bob", 23, "Mathematics"),
    ("Charlie", 26, "Physics"),
    ("Diana", 24, "Computer Science")
]

print("Students:")
for name, age, major in students:
    print(f"{name}, {age}, {major}")

# Application 3: Unique visitors (sets)
daily_visitors = {"Alice", "Bob", "Charlie", "Alice", "Bob"}
print(f"Daily visitors: {daily_visitors}")
print(f"Unique visitors: {len(daily_visitors)}")

# Application 4: Tag system (sets)
blog_posts = {
    "post1": {"python", "programming", "tutorial"},
    "post2": {"python", "data-science", "analysis"},
    "post3": {"javascript", "web", "frontend"}
}

# Find posts with specific tags
python_posts = [post for post, tags in blog_posts.items() if "python" in tags]
print(f"Python posts: {python_posts}")

# 11. When to Use Each Data Structure
print("\n=== When to Use Each Data Structure ===")

# Use lists when:
# - Order matters
# - You need to modify elements
# - You need duplicates
# - You need indexing

shopping_list = ["milk", "bread", "eggs", "milk"]  # Order matters, duplicates allowed
print(f"Shopping list: {shopping_list}")

# Use tuples when:
# - Data shouldn't change
# - You need to use as dictionary keys
# - You need to return multiple values from functions
# - Memory efficiency matters

config = ("localhost", 8080, True)  # Immutable configuration
print(f"Config: {config}")

# Use sets when:
# - You need unique elements
# - You need fast membership testing
# - You need set operations (union, intersection, etc.)

unique_tags = {"python", "programming", "tutorial", "python"}  # Duplicates removed
print(f"Unique tags: {unique_tags}")

# 12. Performance Comparison
print("\n=== Performance Comparison ===")

import time

# Large collections for testing
large_list = list(range(10000))
large_tuple = tuple(range(10000))
large_set = set(range(10000))

# Membership testing performance
test_value = 5000

# List membership (O(n))
start_time = time.time()
is_in_list = test_value in large_list
list_time = time.time() - start_time

# Tuple membership (O(n))
start_time = time.time()
is_in_tuple = test_value in large_tuple
tuple_time = time.time() - start_time

# Set membership (O(1))
start_time = time.time()
is_in_set = test_value in large_set
set_time = time.time() - start_time

print(f"Membership test results:")
print(f"List: {is_in_list} (time: {list_time:.6f}s)")
print(f"Tuple: {is_in_tuple} (time: {tuple_time:.6f}s)")
print(f"Set: {is_in_set} (time: {set_time:.6f}s)")

# 13. Advanced Examples
print("\n=== Advanced Examples ===")

# Example 1: Function returning multiple values
def get_name_and_age():
    return "Alice", 25  # Returns a tuple

name, age = get_name_and_age()  # Tuple unpacking
print(f"Name: {name}, Age: {age}")

# Example 2: Set operations for data analysis
survey_responses = {
    "question1": {"option1", "option2", "option3"},
    "question2": {"option2", "option3", "option4"},
    "question3": {"option1", "option3", "option5"}
}

# Find common options across all questions
common_options = survey_responses["question1"] & survey_responses["question2"] & survey_responses["question3"]
print(f"Common options: {common_options}")

# Find unique options for each question
for question, options in survey_responses.items():
    other_options = set()
    for other_q, other_opts in survey_responses.items():
        if other_q != question:
            other_options.update(other_opts)
    
    unique_options = options - other_options
    print(f"{question} unique options: {unique_options}")

# Example 3: Coordinate system
class Point:
    def __init__(self, x, y):
        self.coords = (x, y)  # Immutable coordinates
    
    def distance_to(self, other):
        return calculate_distance(self.coords, other.coords)
    
    def __repr__(self):
        return f"Point{self.coords}"

p1 = Point(0, 0)
p2 = Point(3, 4)
print(f"Distance from {p1} to {p2}: {p1.distance_to(p2):.2f}")

# Exercises:
"""
1. Create a tuple of your favorite colors and print each one
2. Write a function that takes two sets and returns their intersection
3. Create a program that finds all unique words in a text
4. Write a function that returns the coordinates of a rectangle as a tuple
5. Create a program that tracks unique visitors to a website
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Favorite colors tuple
print("Exercise 1: Favorite Colors")
colors = ("red", "blue", "green", "yellow", "purple")
for color in colors:
    print(f"I like {color}")

# 2. Set intersection function
print("\nExercise 2: Set Intersection")
def find_intersection(set1, set2):
    return set1 & set2

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
intersection = find_intersection(set_a, set_b)
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Intersection: {intersection}")

# 3. Unique words in text
print("\nExercise 3: Unique Words")
text = "python is great python is awesome python is powerful"
words = text.split()
unique_words = set(words)
print(f"Text: {text}")
print(f"Unique words: {unique_words}")

# 4. Rectangle coordinates
print("\nExercise 4: Rectangle Coordinates")
def create_rectangle(x, y, width, height):
    return (x, y, x + width, y + height)

rect = create_rectangle(10, 20, 30, 40)
print(f"Rectangle coordinates: {rect}")

# 5. Website visitor tracking
print("\nExercise 5: Visitor Tracking")
class WebsiteTracker:
    def __init__(self):
        self.visitors = set()
        self.daily_visits = []
    
    def add_visitor(self, visitor_id):
        self.visitors.add(visitor_id)
        self.daily_visits.append(visitor_id)
    
    def get_unique_visitors(self):
        return len(self.visitors)
    
    def get_total_visits(self):
        return len(self.daily_visits)

tracker = WebsiteTracker()
tracker.add_visitor("user1")
tracker.add_visitor("user2")
tracker.add_visitor("user1")  # Duplicate
tracker.add_visitor("user3")

print(f"Unique visitors: {tracker.get_unique_visitors()}")
print(f"Total visits: {tracker.get_total_visits()}")

print("\n🎉 Congratulations! You've completed Lesson 8!")
print("Next: Lesson 9 - Dictionaries")
