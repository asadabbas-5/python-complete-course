# Lesson 22: Generators

"""
This lesson covers:
- What are generators
- Generator functions and yield
- Generator expressions
- Generator methods (send, throw, close)
- Memory efficiency of generators
- Coroutines and async generators
- Practical generator applications
- Best practices and common patterns
"""

# 1. What are Generators
print("=== What are Generators ===")

# Generators are functions that return an iterator
# They use the 'yield' keyword instead of 'return'
# They maintain their state between calls

def simple_generator():
    """A simple generator function"""
    yield 1
    yield 2
    yield 3

# Create a generator
gen = simple_generator()
print(f"Generator object: {gen}")

# Iterate through the generator
for value in gen:
    print(f"Generated value: {value}")

# 2. Generator Functions and yield
print("\n=== Generator Functions and yield ===")

def count_up_to(max_count):
    """Generator that counts up to a maximum"""
    count = 1
    while count <= max_count:
        yield count
        count += 1

# Use the generator
counter = count_up_to(5)
print("Counting up to 5:")
for num in counter:
    print(f"Count: {num}")

# Generator with multiple yields
def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n"""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Generate Fibonacci numbers
fib_gen = fibonacci_generator(20)
print("Fibonacci numbers:")
for num in fib_gen:
    print(f"Fib: {num}")

# 3. Generator Expressions
print("\n=== Generator Expressions ===")

# Generator expression (similar to list comprehension)
squares_gen = (x ** 2 for x in range(5))
print(f"Generator expression: {squares_gen}")

# Convert to list to see values
print(f"Squares: {list(squares_gen)}")

# Generator expression with condition
even_squares = (x ** 2 for x in range(10) if x % 2 == 0)
print(f"Even squares: {list(even_squares)}")

# Memory efficiency comparison
import sys

# List comprehension
squares_list = [x ** 2 for x in range(1000)]
print(f"List size: {sys.getsizeof(squares_list)} bytes")

# Generator expression
squares_gen = (x ** 2 for x in range(1000))
print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")

# 4. Generator Methods
print("\n=== Generator Methods ===")

def interactive_generator():
    """Generator that can receive values"""
    value = yield "First yield"
    print(f"Received: {value}")
    
    value = yield "Second yield"
    print(f"Received: {value}")
    
    yield "Third yield"

# Create generator
gen = interactive_generator()

# Start the generator
print(f"First: {next(gen)}")

# Send value to generator
print(f"Second: {gen.send('Hello')}")

# Send another value
print(f"Third: {gen.send('World')}")

# Generator with throw method
def error_handling_generator():
    """Generator that handles errors"""
    try:
        yield "Normal operation"
        yield "Still normal"
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        yield "Error handled"
    except Exception as e:
        print(f"Caught other error: {e}")
        yield "Other error handled"

# Test error handling
gen = error_handling_generator()
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")

# Throw an error
try:
    gen.throw(ValueError, "Test error")
except StopIteration:
    print("Generator finished")

# Generator with close method
def closable_generator():
    """Generator that can be closed"""
    try:
        yield "First"
        yield "Second"
        yield "Third"
    except GeneratorExit:
        print("Generator is being closed")
        raise

gen = closable_generator()
print(f"First: {next(gen)}")
gen.close()
print("Generator closed")

# 5. Memory Efficiency
print("\n=== Memory Efficiency ===")

def read_large_file(filename):
    """Generator to read large file line by line"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

# Create a sample file
with open("sample.txt", "w") as f:
    for i in range(1000):
        f.write(f"Line {i}: This is line number {i}\n")

# Read file with generator (memory efficient)
print("Reading file with generator:")
line_count = 0
for line in read_large_file("sample.txt"):
    line_count += 1
    if line_count <= 5:  # Show first 5 lines
        print(f"  {line}")

print(f"Total lines read: {line_count}")

# Compare with reading entire file
with open("sample.txt", "r") as f:
    all_lines = f.readlines()
    print(f"All lines in memory: {len(all_lines)}")

# 6. Coroutines and Async Generators
print("\n=== Coroutines and Async Generators ===")

# Coroutine example
def coroutine_generator():
    """Generator that acts as a coroutine"""
    while True:
        value = yield
        print(f"Received: {value}")

# Create coroutine
coro = coroutine_generator()
next(coro)  # Prime the coroutine

# Send values
coro.send("Hello")
coro.send("World")
coro.send("Python")

# Async generator (Python 3.6+)
import asyncio

async def async_generator():
    """Async generator example"""
    for i in range(5):
        await asyncio.sleep(0.1)  # Simulate async operation
        yield i

async def use_async_generator():
    """Use async generator"""
    async for value in async_generator():
        print(f"Async value: {value}")

# Run async generator
asyncio.run(use_async_generator())

# 7. Practical Generator Applications
print("\n=== Practical Generator Applications ===")

# Application 1: Data Processing Pipeline
def data_source():
    """Simulate data source"""
    for i in range(10):
        yield {"id": i, "value": i * 2, "status": "active" if i % 2 == 0 else "inactive"}

def filter_active(data_gen):
    """Filter only active records"""
    for record in data_gen:
        if record["status"] == "active":
            yield record

def transform_data(data_gen):
    """Transform data"""
    for record in data_gen:
        record["processed_value"] = record["value"] * 10
        yield record

# Create pipeline
pipeline = transform_data(filter_active(data_source()))

print("Data pipeline results:")
for record in pipeline:
    print(f"  {record}")

# Application 2: Infinite Sequences
def infinite_counter(start=0, step=1):
    """Generate infinite sequence"""
    current = start
    while True:
        yield current
        current += step

def take(n, generator):
    """Take first n items from generator"""
    for i, item in enumerate(generator):
        if i >= n:
            break
        yield item

# Generate infinite sequence
counter = infinite_counter(10, 5)
first_5 = take(5, counter)
print(f"First 5 values: {list(first_5)}")

# Application 3: File Processing
def process_log_file(filename):
    """Process log file with generator"""
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if line.strip():  # Skip empty lines
                    yield {
                        'line_number': line_num,
                        'content': line.strip(),
                        'timestamp': f"2024-01-15 {line_num:02d}:00:00"
                    }
    except FileNotFoundError:
        print(f"File {filename} not found")

# Process log file
log_processor = process_log_file("sample.txt")
print("Log processing:")
for i, log_entry in enumerate(log_processor):
    if i < 3:  # Show first 3 entries
        print(f"  {log_entry}")
    else:
        break

# 8. Generator Patterns
print("\n=== Generator Patterns ===")

# Pattern 1: Generator Chain
def chain_generators(*generators):
    """Chain multiple generators together"""
    for gen in generators:
        yield from gen

gen1 = (x for x in range(3))
gen2 = (x for x in range(3, 6))
gen3 = (x for x in range(6, 9))

chained = chain_generators(gen1, gen2, gen3)
print(f"Chained generators: {list(chained)}")

# Pattern 2: Generator Tee (split generator)
def tee_generator(gen, n=2):
    """Split a generator into multiple generators"""
    # This is a simplified version
    items = list(gen)
    for i in range(n):
        yield iter(items)

# Pattern 3: Generator Groupby
def groupby_generator(iterable, key_func=None):
    """Group items by key function"""
    if key_func is None:
        key_func = lambda x: x
    
    current_key = None
    current_group = []
    
    for item in iterable:
        item_key = key_func(item)
        
        if current_key is None or current_key == item_key:
            current_group.append(item)
            current_key = item_key
        else:
            yield current_key, current_group
            current_group = [item]
            current_key = item_key
    
    if current_group:
        yield current_key, current_group

# Test groupby
data = [1, 1, 2, 2, 2, 3, 3]
grouped = groupby_generator(data)
print("Grouped data:")
for key, group in grouped:
    print(f"  {key}: {group}")

# 9. Advanced Generator Techniques
print("\n=== Advanced Generator Techniques ===")

# Generator with state
class StatefulGenerator:
    """Generator that maintains state"""
    
    def __init__(self, initial_state=0):
        self.state = initial_state
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.state += 1
        if self.state > 10:
            raise StopIteration
        return self.state

# Use stateful generator
stateful = StatefulGenerator(5)
print(f"Stateful generator: {list(stateful)}")

# Generator with context manager
def generator_with_context():
    """Generator that works with context manager"""
    print("Generator started")
    try:
        for i in range(5):
            yield i
    finally:
        print("Generator finished")

# Use generator with context
gen = generator_with_context()
try:
    for value in gen:
        print(f"Value: {value}")
        if value == 2:
            break
finally:
    gen.close()

# 10. Performance Considerations
print("\n=== Performance Considerations ===")

import time

# Compare generator vs list for large datasets
def generate_large_list(n):
    """Generate large list"""
    return [x ** 2 for x in range(n)]

def generate_large_generator(n):
    """Generate large generator"""
    return (x ** 2 for x in range(n))

# Test with large dataset
n = 1000000

# List approach
start_time = time.time()
squares_list = generate_large_list(n)
list_time = time.time() - start_time
print(f"List generation time: {list_time:.4f}s")

# Generator approach
start_time = time.time()
squares_gen = generate_large_generator(n)
gen_time = time.time() - start_time
print(f"Generator creation time: {gen_time:.4f}s")

# Memory usage
print(f"List memory usage: {sys.getsizeof(squares_list)} bytes")
print(f"Generator memory usage: {sys.getsizeof(squares_gen)} bytes")

# 11. Best Practices
print("\n=== Best Practices ===")

# Best Practice 1: Use generators for large datasets
def process_large_dataset(data):
    """Process large dataset efficiently"""
    for item in data:
        # Process item
        yield item * 2

# Best Practice 2: Use yield from for delegation
def delegating_generator():
    """Generator that delegates to another generator"""
    yield from range(5)
    yield from [10, 20, 30]

print(f"Delegating generator: {list(delegating_generator())}")

# Best Practice 3: Handle exceptions properly
def safe_generator():
    """Generator with proper exception handling"""
    try:
        for i in range(5):
            yield i
    except Exception as e:
        print(f"Error in generator: {e}")
        raise

# Best Practice 4: Use generators for infinite sequences
def infinite_fibonacci():
    """Generate infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take first 10 Fibonacci numbers
fib_gen = infinite_fibonacci()
first_10_fib = [next(fib_gen) for _ in range(10)]
print(f"First 10 Fibonacci numbers: {first_10_fib}")

# 12. Real-world Examples
print("\n=== Real-world Examples ===")

# Example 1: Data Streaming
def stream_data(source):
    """Stream data from source"""
    for chunk in source:
        yield chunk

def process_chunk(chunk):
    """Process a chunk of data"""
    return chunk.upper()

def data_stream_processor():
    """Process streaming data"""
    data_source = ["chunk1", "chunk2", "chunk3", "chunk4"]
    
    for chunk in stream_data(data_source):
        processed = process_chunk(chunk)
        yield processed

print("Streaming data processing:")
for processed_chunk in data_stream_processor():
    print(f"  Processed: {processed_chunk}")

# Example 2: Batch Processing
def batch_processor(items, batch_size=3):
    """Process items in batches"""
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    
    if batch:  # Yield remaining items
        yield batch

items = list(range(10))
print("Batch processing:")
for batch in batch_processor(items, 3):
    print(f"  Batch: {batch}")

# Example 3: Data Validation Pipeline
def validate_data(data_gen):
    """Validate data in pipeline"""
    for item in data_gen:
        if isinstance(item, dict) and 'id' in item:
            yield item
        else:
            print(f"Invalid item: {item}")

def enrich_data(data_gen):
    """Enrich data with additional fields"""
    for item in data_gen:
        item['enriched'] = True
        item['timestamp'] = '2024-01-15'
        yield item

# Create validation pipeline
raw_data = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    'invalid',
    {'id': 3, 'name': 'Charlie'}
]

pipeline = enrich_data(validate_data(iter(raw_data)))
print("Validation pipeline:")
for item in pipeline:
    print(f"  {item}")

# Cleanup
import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")

# Exercises:
"""
1. Create a generator that yields prime numbers
2. Write a generator that reads a file line by line
3. Create a generator that generates random numbers
4. Write a generator that yields Fibonacci numbers
5. Create a generator that processes data in batches
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Prime number generator
print("Exercise 1: Prime Number Generator")
def prime_generator(limit):
    """Generate prime numbers up to limit"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, limit):
        if is_prime(num):
            yield num

primes = prime_generator(20)
print(f"Primes up to 20: {list(primes)}")

# 2. File line reader
print("\nExercise 2: File Line Reader")
def file_line_reader(filename):
    """Read file line by line"""
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                yield line_num, line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

# Create test file
with open("test.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

reader = file_line_reader("test.txt")
print("File lines:")
for line_num, line in reader:
    print(f"  {line_num}: {line}")

# 3. Random number generator
print("\nExercise 3: Random Number Generator")
def random_number_generator(limit=10):
    """Generate random numbers"""
    import random
    for _ in range(limit):
        yield random.randint(1, 100)

random_gen = random_number_generator(5)
print(f"Random numbers: {list(random_gen)}")

# 4. Fibonacci generator
print("\nExercise 4: Fibonacci Generator")
def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n"""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator(50)
print(f"Fibonacci numbers up to 50: {list(fib_gen)}")

# 5. Batch processor
print("\nExercise 5: Batch Processor")
def batch_processor(items, batch_size):
    """Process items in batches"""
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    
    if batch:
        yield batch

items = list(range(10))
batches = batch_processor(items, 3)
print("Batches:")
for batch in batches:
    print(f"  {batch}")

# Cleanup
if os.path.exists("test.txt"):
    os.remove("test.txt")

print("\n🎉 Congratulations! You've completed Lesson 22!")
print("Next: Lesson 23 - Context Managers")
