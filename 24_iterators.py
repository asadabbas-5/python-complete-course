# Lesson 24: Iterators

"""
This lesson covers:
- What are iterators
- Iterator protocol
- Creating custom iterators
- Iterator vs iterable
- Built-in iterator functions
- Iterator patterns and best practices
- Performance considerations
- Practical iterator examples
"""

# 1. What are Iterators
print("=== What are Iterators ===")

# An iterator is an object that implements the iterator protocol
# It has __iter__() and __next__() methods

# Basic iterator example
class SimpleIterator:
    """A simple iterator class"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Use the iterator
iterator = SimpleIterator([1, 2, 3, 4, 5])
for value in iterator:
    print(f"Value: {value}")

# 2. Iterator Protocol
print("\n=== Iterator Protocol ===")

# The iterator protocol requires two methods:
# __iter__() - returns the iterator object itself
# __next__() - returns the next value or raises StopIteration

class CounterIterator:
    """Iterator that counts up to a limit"""
    
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Test the iterator
counter = CounterIterator(5)
print("Counter iterator:")
for i in counter:
    print(f"Count: {i}")

# Manual iteration
counter = CounterIterator(3)
print("Manual iteration:")
print(f"Next: {next(counter)}")
print(f"Next: {next(counter)}")
print(f"Next: {next(counter)}")

try:
    print(f"Next: {next(counter)}")
except StopIteration:
    print("Iterator exhausted")

# 3. Iterator vs Iterable
print("\n=== Iterator vs Iterable ===")

# Iterable: An object that can be iterated over (has __iter__ method)
# Iterator: An object that implements the iterator protocol

class IterableClass:
    """A class that is iterable but not an iterator"""
    
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return IteratorClass(self.data)

class IteratorClass:
    """A class that implements the iterator protocol"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Test iterable vs iterator
iterable = IterableClass([10, 20, 30])
print("Iterable class:")
for value in iterable:
    print(f"Value: {value}")

# Multiple iterations of the same iterable
print("Multiple iterations:")
for value in iterable:
    print(f"First iteration: {value}")

for value in iterable:
    print(f"Second iteration: {value}")

# 4. Creating Custom Iterators
print("\n=== Creating Custom Iterators ===")

# Iterator for Fibonacci sequence
class FibonacciIterator:
    """Iterator that generates Fibonacci numbers"""
    
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

# Use Fibonacci iterator
fib_iter = FibonacciIterator(10)
print("Fibonacci sequence:")
for num in fib_iter:
    print(f"Fib: {num}")

# Iterator for file lines
class FileLineIterator:
    """Iterator that reads file lines"""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
        
        line = self.file.readline()
        if not line:
            self.file.close()
            self.file = None
            raise StopIteration
        
        return line.strip()

# Create test file
with open("test_file.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")

# Use file line iterator
file_iter = FileLineIterator("test_file.txt")
print("File lines:")
for line in file_iter:
    print(f"Line: {line}")

# 5. Built-in Iterator Functions
print("\n=== Built-in Iterator Functions ===")

# iter() function
data = [1, 2, 3, 4, 5]
iterator = iter(data)
print(f"Iterator: {iterator}")

# next() function
print(f"Next: {next(iterator)}")
print(f"Next: {next(iterator)}")

# enumerate() function
print("Enumerate:")
for index, value in enumerate(['a', 'b', 'c']):
    print(f"Index: {index}, Value: {value}")

# zip() function
print("Zip:")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item1, item2 in zip(list1, list2):
    print(f"Item1: {item1}, Item2: {item2}")

# reversed() function
print("Reversed:")
for value in reversed([1, 2, 3, 4, 5]):
    print(f"Reversed: {value}")

# sorted() function
print("Sorted:")
data = [3, 1, 4, 1, 5, 9, 2, 6]
for value in sorted(data):
    print(f"Sorted: {value}")

# 6. Iterator Patterns
print("\n=== Iterator Patterns ===")

# Pattern 1: Iterator with state
class StatefulIterator:
    """Iterator that maintains state between calls"""
    
    def __init__(self, initial_state):
        self.state = initial_state
        self.done = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.done:
            raise StopIteration
        
        if self.state >= 10:
            self.done = True
            raise StopIteration
        
        self.state += 1
        return self.state - 1

# Use stateful iterator
stateful = StatefulIterator(5)
print("Stateful iterator:")
for value in stateful:
    print(f"Value: {value}")

# Pattern 2: Iterator with cleanup
class CleanupIterator:
    """Iterator with cleanup operations"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.cleanup_done = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            self._cleanup()
            raise StopIteration
        
        value = self.data[self.index]
        self.index += 1
        return value
    
    def _cleanup(self):
        if not self.cleanup_done:
            print("Cleaning up iterator")
            self.cleanup_done = True

# Use cleanup iterator
cleanup_iter = CleanupIterator([1, 2, 3])
print("Cleanup iterator:")
for value in cleanup_iter:
    print(f"Value: {value}")

# Pattern 3: Iterator with error handling
class ErrorHandlingIterator:
    """Iterator with error handling"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        try:
            value = self.data[self.index]
            self.index += 1
            return value
        except Exception as e:
            print(f"Error processing item at index {self.index}: {e}")
            self.index += 1
            return None

# Test error handling iterator
error_data = [1, 2, "error", 4, 5]
error_iter = ErrorHandlingIterator(error_data)
print("Error handling iterator:")
for value in error_iter:
    print(f"Value: {value}")

# 7. Advanced Iterator Techniques
print("\n=== Advanced Iterator Techniques ===")

# Iterator with custom behavior
class CustomIterator:
    """Iterator with custom behavior"""
    
    def __init__(self, data, step=1):
        self.data = data
        self.step = step
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        value = self.data[self.index]
        self.index += self.step
        return value
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]

# Use custom iterator
custom_iter = CustomIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], step=2)
print("Custom iterator (step=2):")
for value in custom_iter:
    print(f"Value: {value}")

# Iterator with filtering
class FilteringIterator:
    """Iterator that filters values"""
    
    def __init__(self, data, filter_func):
        self.data = data
        self.filter_func = filter_func
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            if self.filter_func(value):
                return value
        
        raise StopIteration

# Use filtering iterator
filter_iter = FilteringIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x % 2 == 0)
print("Filtering iterator (even numbers):")
for value in filter_iter:
    print(f"Value: {value}")

# 8. Iterator Performance Considerations
print("\n=== Iterator Performance Considerations ===")

import time
import sys

# Compare iterator vs list for memory usage
def create_list(n):
    """Create a list of n elements"""
    return [i for i in range(n)]

def create_iterator(n):
    """Create an iterator of n elements"""
    return iter(range(n))

# Memory usage comparison
n = 1000000

# List memory usage
list_data = create_list(n)
list_memory = sys.getsizeof(list_data)
print(f"List memory usage: {list_memory} bytes")

# Iterator memory usage
iter_data = create_iterator(n)
iter_memory = sys.getsizeof(iter_data)
print(f"Iterator memory usage: {iter_memory} bytes")

# Performance comparison
def sum_list(data):
    """Sum elements in a list"""
    return sum(data)

def sum_iterator(data):
    """Sum elements in an iterator"""
    return sum(data)

# Test with smaller dataset for timing
n = 100000
list_data = create_list(n)
iter_data = create_iterator(n)

# Time list sum
start_time = time.time()
list_sum = sum_list(list_data)
list_time = time.time() - start_time

# Time iterator sum
start_time = time.time()
iter_sum = sum_iterator(iter_data)
iter_time = time.time() - start_time

print(f"List sum time: {list_time:.4f}s")
print(f"Iterator sum time: {iter_time:.4f}s")

# 9. Iterator Best Practices
print("\n=== Iterator Best Practices ===")

# Best Practice 1: Always implement both __iter__ and __next__
class ProperIterator:
    """Iterator that follows best practices"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Best Practice 2: Handle StopIteration properly
class StopIterationHandler:
    """Iterator that handles StopIteration properly"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration  # This is the correct way to signal end
        value = self.data[self.index]
        self.index += 1
        return value

# Best Practice 3: Use iter() and next() for manual iteration
data = [1, 2, 3, 4, 5]
iterator = iter(data)

try:
    while True:
        value = next(iterator)
        print(f"Manual iteration: {value}")
except StopIteration:
    print("Iterator exhausted")

# Best Practice 4: Implement __len__ when possible
class SizedIterator:
    """Iterator that implements __len__"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
    
    def __len__(self):
        return len(self.data)

# Test sized iterator
sized_iter = SizedIterator([1, 2, 3, 4, 5])
print(f"Iterator length: {len(sized_iter)}")

# 10. Practical Iterator Examples
print("\n=== Practical Iterator Examples ===")

# Example 1: Database Result Iterator
class DatabaseResultIterator:
    """Iterator for database query results"""
    
    def __init__(self, query_results):
        self.query_results = query_results
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.query_results):
            raise StopIteration
        
        result = self.query_results[self.index]
        self.index += 1
        return result

# Simulate database results
db_results = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 35}
]

db_iter = DatabaseResultIterator(db_results)
print("Database results:")
for result in db_iter:
    print(f"User: {result['name']}, Age: {result['age']}")

# Example 2: File Processing Iterator
class FileProcessorIterator:
    """Iterator for processing file chunks"""
    
    def __init__(self, filename, chunk_size=1024):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file = None
        self.position = 0
    
    def __iter__(self):
        self.file = open(self.filename, 'rb')
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
        
        chunk = self.file.read(self.chunk_size)
        if not chunk:
            self.file.close()
            self.file = None
            raise StopIteration
        
        self.position += len(chunk)
        return chunk

# Create test file
with open("test_chunks.txt", "w") as f:
    f.write("This is a test file with multiple lines.\n" * 10)

# Use file processor iterator
file_iter = FileProcessorIterator("test_chunks.txt", chunk_size=50)
print("File chunks:")
for i, chunk in enumerate(file_iter):
    print(f"Chunk {i}: {chunk.decode('utf-8')[:20]}...")

# Example 3: API Response Iterator
class APIResponseIterator:
    """Iterator for API responses with pagination"""
    
    def __init__(self, api_client, endpoint):
        self.api_client = api_client
        self.endpoint = endpoint
        self.page = 1
        self.current_data = []
        self.data_index = 0
        self.has_more = True
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.has_more:
            raise StopIteration
        
        # Load new page if needed
        if self.data_index >= len(self.current_data):
            self.current_data = self._fetch_page(self.page)
            if not self.current_data:
                self.has_more = False
                raise StopIteration
            self.page += 1
            self.data_index = 0
        
        # Return next item
        item = self.current_data[self.data_index]
        self.data_index += 1
        return item
    
    def _fetch_page(self, page):
        """Simulate API call"""
        # Simulate API response
        if page <= 3:
            return [f"Item {page}-{i}" for i in range(1, 4)]
        return []

# Use API response iterator
class MockAPIClient:
    def get(self, endpoint, page):
        return f"API call to {endpoint}, page {page}"

api_iter = APIResponseIterator(MockAPIClient(), "/users")
print("API responses:")
for item in api_iter:
    print(f"API item: {item}")

# 11. Iterator Testing
print("\n=== Iterator Testing ===")

# Test iterator behavior
class TestableIterator:
    """Iterator designed for testing"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.iterations = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        self.iterations += 1
        value = self.data[self.index]
        self.index += 1
        return value

# Test iterator
test_iter = TestableIterator([1, 2, 3, 4, 5])
print("Testing iterator:")
for value in test_iter:
    print(f"Value: {value}")

print(f"Total iterations: {test_iter.iterations}")

# Test iterator exhaustion
test_iter = TestableIterator([1, 2, 3])
print("Testing iterator exhaustion:")
for value in test_iter:
    print(f"Value: {value}")

try:
    next(test_iter)
except StopIteration:
    print("Iterator properly exhausted")

# 12. Real-world Iterator Examples
print("\n=== Real-world Iterator Examples ===")

# Example 1: Configuration Iterator
class ConfigIterator:
    """Iterator for configuration settings"""
    
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.keys = list(config_dict.keys())
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        
        key = self.keys[self.index]
        value = self.config_dict[key]
        self.index += 1
        return key, value

# Use configuration iterator
config = {
    "database_url": "sqlite:///app.db",
    "debug": True,
    "port": 8080,
    "host": "localhost"
}

config_iter = ConfigIterator(config)
print("Configuration settings:")
for key, value in config_iter:
    print(f"  {key}: {value}")

# Example 2: Log Entry Iterator
class LogEntryIterator:
    """Iterator for log entries"""
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.file = None
        self.line_number = 0
    
    def __iter__(self):
        self.file = open(self.log_file, 'r')
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
        
        line = self.file.readline()
        if not line:
            self.file.close()
            self.file = None
            raise StopIteration
        
        self.line_number += 1
        return {
            'line_number': self.line_number,
            'content': line.strip(),
            'timestamp': f"2024-01-15 {self.line_number:02d}:00:00"
        }

# Use log entry iterator
log_iter = LogEntryIterator("test_chunks.txt")
print("Log entries:")
for i, entry in enumerate(log_iter):
    if i < 3:  # Show first 3 entries
        print(f"  {entry}")
    else:
        break

# Cleanup
import os
files_to_remove = ["test_file.txt", "test_chunks.txt"]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)

# Exercises:
"""
1. Create an iterator that generates prime numbers
2. Write an iterator that reads a file line by line
3. Create an iterator that generates random numbers
4. Write an iterator that processes data in batches
5. Create an iterator that filters values based on a condition
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Prime number iterator
print("Exercise 1: Prime Number Iterator")
class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current < self.limit:
            if self._is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration
    
    def _is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

prime_iter = PrimeIterator(20)
print(f"Primes up to 20: {list(prime_iter)}")

# 2. File line iterator
print("\nExercise 2: File Line Iterator")
class FileLineIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
        
        line = self.file.readline()
        if not line:
            self.file.close()
            self.file = None
            raise StopIteration
        
        return line.strip()

# Create test file
with open("test_lines.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

line_iter = FileLineIterator("test_lines.txt")
print("File lines:")
for line in line_iter:
    print(f"  {line}")

# 3. Random number iterator
print("\nExercise 3: Random Number Iterator")
class RandomIterator:
    def __init__(self, count, min_val=1, max_val=100):
        self.count = count
        self.min_val = min_val
        self.max_val = max_val
        self.generated = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.generated >= self.count:
            raise StopIteration
        
        import random
        self.generated += 1
        return random.randint(self.min_val, self.max_val)

random_iter = RandomIterator(5)
print(f"Random numbers: {list(random_iter)}")

# 4. Batch processor iterator
print("\nExercise 4: Batch Processor Iterator")
class BatchIterator:
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        batch = self.data[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return batch

batch_iter = BatchIterator(list(range(10)), 3)
print("Batches:")
for batch in batch_iter:
    print(f"  {batch}")

# 5. Filtering iterator
print("\nExercise 5: Filtering Iterator")
class FilterIterator:
    def __init__(self, data, filter_func):
        self.data = data
        self.filter_func = filter_func
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            if self.filter_func(value):
                return value
        raise StopIteration

filter_iter = FilterIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x % 2 == 0)
print(f"Even numbers: {list(filter_iter)}")

# Cleanup
if os.path.exists("test_lines.txt"):
    os.remove("test_lines.txt")

print("\n🎉 Congratulations! You've completed Lesson 24!")
print("Next: Lesson 25 - Metaclasses")
