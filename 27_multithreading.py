# Lesson 27: Multithreading

"""
This lesson covers:
- What is multithreading
- Threading module
- Thread creation and management
- Thread synchronization
- Locks and semaphores
- Thread communication
- Thread pools
- GIL (Global Interpreter Lock)
- When to use threading vs asyncio
- Practical threading examples
"""

# 1. What is Multithreading
print("=== What is Multithreading ===")

# Multithreading allows multiple threads to run concurrently
# Each thread can execute different parts of the program

import threading
import time
import random

# Simple thread example
def worker_thread(name, delay):
    print(f"Thread {name} starting")
    time.sleep(delay)
    print(f"Thread {name} completed")

# Create and start threads
thread1 = threading.Thread(target=worker_thread, args=("A", 1))
thread2 = threading.Thread(target=worker_thread, args=("B", 2))

print("Starting threads...")
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
print("All threads completed")

# 2. Threading Module
print("\n=== Threading Module ===")

# Thread class
class CustomThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        print(f"Custom thread {self.name} starting")
        time.sleep(self.delay)
        print(f"Custom thread {self.name} completed")

# Create and start custom threads
custom_thread1 = CustomThread("Custom-A", 1)
custom_thread2 = CustomThread("Custom-B", 1.5)

custom_thread1.start()
custom_thread2.start()

custom_thread1.join()
custom_thread2.join()

# 3. Thread Creation and Management
print("\n=== Thread Creation and Management ===")

# Thread attributes
def thread_info():
    current_thread = threading.current_thread()
    print(f"Current thread: {current_thread.name}")
    print(f"Thread ID: {current_thread.ident}")
    print(f"Is alive: {current_thread.is_alive()}")
    print(f"Is daemon: {current_thread.daemon}")

# Main thread info
thread_info()

# Create new thread
new_thread = threading.Thread(target=thread_info, name="InfoThread")
new_thread.start()
new_thread.join()

# Thread enumeration
print(f"Active threads: {threading.active_count()}")
print(f"Thread names: {[t.name for t in threading.enumerate()]}")

# 4. Thread Synchronization
print("\n=== Thread Synchronization ===")

# Shared resource
shared_counter = 0

# Unsynchronized function
def unsynchronized_increment():
    global shared_counter
    for _ in range(1000):
        shared_counter += 1

# Synchronized function
def synchronized_increment(lock):
    global shared_counter
    for _ in range(1000):
        with lock:
            shared_counter += 1

# Test unsynchronized access
shared_counter = 0
threads = []
for i in range(5):
    thread = threading.Thread(target=unsynchronized_increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Unsynchronized counter: {shared_counter}")

# Test synchronized access
shared_counter = 0
lock = threading.Lock()
threads = []
for i in range(5):
    thread = threading.Thread(target=synchronized_increment, args=(lock,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Synchronized counter: {shared_counter}")

# 5. Locks and Semaphores
print("\n=== Locks and Semaphores ===")

# Lock example
def lock_example():
    lock = threading.Lock()
    
    def critical_section(thread_id):
        print(f"Thread {thread_id} waiting for lock")
        with lock:
            print(f"Thread {thread_id} acquired lock")
            time.sleep(0.1)
            print(f"Thread {thread_id} releasing lock")
    
    threads = []
    for i in range(3):
        thread = threading.Thread(target=critical_section, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

lock_example()

# RLock (Reentrant Lock) example
def rlock_example():
    rlock = threading.RLock()
    
    def recursive_function(count):
        with rlock:
            if count > 0:
                print(f"Recursive call {count}")
                recursive_function(count - 1)
    
    thread = threading.Thread(target=recursive_function, args=(3,))
    thread.start()
    thread.join()

rlock_example()

# Semaphore example
def semaphore_example():
    semaphore = threading.Semaphore(2)  # Allow 2 threads at a time
    
    def worker(worker_id):
        print(f"Worker {worker_id} waiting for semaphore")
        with semaphore:
            print(f"Worker {worker_id} acquired semaphore")
            time.sleep(1)
            print(f"Worker {worker_id} releasing semaphore")
    
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

semaphore_example()

# 6. Thread Communication
print("\n=== Thread Communication ===")

# Event example
def event_example():
    event = threading.Event()
    
    def waiter():
        print("Waiter waiting for event")
        event.wait()
        print("Waiter received event")
    
    def setter():
        time.sleep(2)
        print("Setter setting event")
        event.set()
    
    waiter_thread = threading.Thread(target=waiter)
    setter_thread = threading.Thread(target=setter)
    
    waiter_thread.start()
    setter_thread.start()
    
    waiter_thread.join()
    setter_thread.join()

event_example()

# Condition example
def condition_example():
    condition = threading.Condition()
    shared_data = []
    
    def producer():
        with condition:
            time.sleep(1)
            shared_data.append("data")
            print("Producer produced data")
            condition.notify()
    
    def consumer():
        with condition:
            while not shared_data:
                print("Consumer waiting for data")
                condition.wait()
            data = shared_data.pop()
            print(f"Consumer consumed: {data}")
    
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    consumer_thread.start()
    producer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()

condition_example()

# Queue example
def queue_example():
    import queue
    
    q = queue.Queue()
    
    def producer():
        for i in range(5):
            q.put(f"item-{i}")
            print(f"Produced: item-{i}")
            time.sleep(0.1)
        q.put(None)  # Signal end
    
    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            print(f"Consumed: {item}")
            time.sleep(0.1)
            q.task_done()
    
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()

queue_example()

# 7. Thread Pools
print("\n=== Thread Pools ===")

# ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

def thread_pool_example():
    def worker(task_id):
        print(f"Worker {task_id} starting")
        time.sleep(1)
        print(f"Worker {task_id} completed")
        return f"Result from worker {task_id}"
    
    # Create thread pool
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks
        futures = [executor.submit(worker, i) for i in range(5)]
        
        # Get results
        results = [future.result() for future in futures]
        print(f"Results: {results}")

thread_pool_example()

# Thread pool with map
def thread_pool_map_example():
    def process_item(item):
        time.sleep(0.1)
        return f"Processed {item}"
    
    items = [1, 2, 3, 4, 5]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_item, items))
        print(f"Map results: {results}")

thread_pool_map_example()

# 8. GIL (Global Interpreter Lock)
print("\n=== GIL (Global Interpreter Lock) ===")

# GIL prevents true parallelism for CPU-bound tasks
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

# Test CPU-bound performance
def test_cpu_bound():
    start_time = time.time()
    
    # Sequential execution
    results = [cpu_bound_task(1000000) for _ in range(4)]
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f}s")
    
    # Threaded execution (limited by GIL)
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_bound_task, 1000000) for _ in range(4)]
        results = [future.result() for future in futures]
    
    threaded_time = time.time() - start_time
    print(f"Threaded time: {threaded_time:.2f}s")
    print(f"Performance ratio: {sequential_time/threaded_time:.2f}")

test_cpu_bound()

# I/O-bound tasks benefit from threading
def io_bound_task(delay):
    time.sleep(delay)
    return f"IO task completed after {delay}s"

def test_io_bound():
    start_time = time.time()
    
    # Sequential execution
    results = [io_bound_task(0.1) for _ in range(5)]
    
    sequential_time = time.time() - start_time
    print(f"Sequential IO time: {sequential_time:.2f}s")
    
    # Threaded execution
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(io_bound_task, 0.1) for _ in range(5)]
        results = [future.result() for future in futures]
    
    threaded_time = time.time() - start_time
    print(f"Threaded IO time: {threaded_time:.2f}s")
    print(f"Performance ratio: {sequential_time/threaded_time:.2f}")

test_io_bound()

# 9. When to Use Threading vs Asyncio
print("\n=== When to Use Threading vs Asyncio ===")

# Threading is good for:
# - I/O-bound tasks
# - CPU-bound tasks (with multiprocessing)
# - Legacy code integration
# - Blocking operations

# Asyncio is good for:
# - I/O-bound tasks
# - Network operations
# - Event-driven programming
# - Single-threaded concurrency

def threading_vs_asyncio_example():
    # Threading approach
    def threaded_io_task():
        start_time = time.time()
        
        def io_operation(delay):
            time.sleep(delay)
            return f"IO operation completed after {delay}s"
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(io_operation, 0.1) for _ in range(3)]
            results = [future.result() for future in futures]
        
        threading_time = time.time() - start_time
        print(f"Threading approach: {threading_time:.2f}s")
        return results
    
    # Asyncio approach
    async def asyncio_io_task():
        start_time = time.time()
        
        async def io_operation(delay):
            await asyncio.sleep(delay)
            return f"IO operation completed after {delay}s"
        
        tasks = [io_operation(0.1) for _ in range(3)]
        results = await asyncio.gather(*tasks)
        
        asyncio_time = time.time() - start_time
        print(f"Asyncio approach: {asyncio_time:.2f}s")
        return results
    
    # Test both approaches
    threading_results = threaded_io_task()
    asyncio_results = asyncio.run(asyncio_io_task())
    
    print(f"Threading results: {threading_results}")
    print(f"Asyncio results: {asyncio_results}")

threading_vs_asyncio_example()

# 10. Practical Threading Examples
print("\n=== Practical Threading Examples ===")

# Example 1: Web Scraper with Threading
def web_scraper_example():
    import urllib.request
    import urllib.parse
    
    def fetch_url(url):
        try:
            with urllib.request.urlopen(url) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"Error fetching {url}: {e}"
    
    urls = [
        "http://httpbin.org/json",
        "http://httpbin.org/uuid",
        "http://httpbin.org/ip"
    ]
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(fetch_url, url) for url in urls]
        results = [future.result() for future in futures]
    
    threading_time = time.time() - start_time
    print(f"Web scraper time: {threading_time:.2f}s")
    print("Web scraper results:")
    for i, result in enumerate(results):
        print(f"  URL {i+1}: {result[:50]}...")

web_scraper_example()

# Example 2: File Processing with Threading
def file_processing_example():
    def process_file(filename):
        time.sleep(0.1)  # Simulate file processing
        return f"Processed {filename}"
    
    filenames = [f"file{i}.txt" for i in range(10)]
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_file, filename) for filename in filenames]
        results = [future.result() for future in futures]
    
    threading_time = time.time() - start_time
    print(f"File processing time: {threading_time:.2f}s")
    print("File processing results:")
    for result in results:
        print(f"  {result}")

file_processing_example()

# Example 3: Database Operations with Threading
def database_operations_example():
    def db_query(query):
        time.sleep(0.1)  # Simulate database delay
        return f"Result for: {query}"
    
    queries = [
        "SELECT * FROM users",
        "SELECT * FROM orders",
        "SELECT * FROM products",
        "SELECT * FROM categories"
    ]
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(db_query, query) for query in queries]
        results = [future.result() for future in futures]
    
    threading_time = time.time() - start_time
    print(f"Database operations time: {threading_time:.2f}s")
    print("Database results:")
    for result in results:
        print(f"  {result}")

database_operations_example()

# 11. Thread Safety
print("\n=== Thread Safety ===")

# Thread-safe counter
class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def decrement(self):
        with self._lock:
            self._value -= 1
    
    def get_value(self):
        with self._lock:
            return self._value

def thread_safety_example():
    counter = ThreadSafeCounter()
    
    def worker():
        for _ in range(1000):
            counter.increment()
    
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Thread-safe counter value: {counter.get_value()}")

thread_safety_example()

# Thread-safe queue
def thread_safe_queue_example():
    import queue
    
    q = queue.Queue()
    
    def producer():
        for i in range(10):
            q.put(f"item-{i}")
            print(f"Produced: item-{i}")
            time.sleep(0.1)
    
    def consumer():
        while True:
            try:
                item = q.get(timeout=1)
                print(f"Consumed: {item}")
                time.sleep(0.1)
                q.task_done()
            except queue.Empty:
                break
    
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()

thread_safe_queue_example()

# 12. Thread Debugging
print("\n=== Thread Debugging ===")

# Thread debugging techniques
def thread_debugging_example():
    def worker_with_debug(worker_id):
        print(f"Worker {worker_id} starting")
        try:
            time.sleep(0.1)
            if worker_id == 2:
                raise Exception(f"Error in worker {worker_id}")
            print(f"Worker {worker_id} completed successfully")
        except Exception as e:
            print(f"Worker {worker_id} failed: {e}")
    
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker_with_debug, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

thread_debugging_example()

# Thread monitoring
def thread_monitoring_example():
    def monitor_threads():
        while True:
            active_threads = threading.active_count()
            thread_names = [t.name for t in threading.enumerate()]
            print(f"Active threads: {active_threads}, Names: {thread_names}")
            time.sleep(0.5)
    
    def worker():
        time.sleep(2)
        print("Worker completed")
    
    monitor_thread = threading.Thread(target=monitor_threads, daemon=True)
    worker_thread = threading.Thread(target=worker)
    
    monitor_thread.start()
    worker_thread.start()
    
    worker_thread.join()

thread_monitoring_example()

# Exercises:
"""
1. Create a thread-safe bank account class
2. Write a multithreaded web scraper
3. Create a thread pool for image processing
4. Write a producer-consumer pattern with threading
5. Create a thread-safe cache implementation
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Thread-safe bank account
print("Exercise 1: Thread-safe Bank Account")
class ThreadSafeBankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._lock = threading.Lock()
    
    def deposit(self, amount):
        with self._lock:
            self._balance += amount
            print(f"Deposited {amount}, balance: {self._balance}")
    
    def withdraw(self, amount):
        with self._lock:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrew {amount}, balance: {self._balance}")
                return True
            else:
                print(f"Insufficient funds for withdrawal of {amount}")
                return False
    
    def get_balance(self):
        with self._lock:
            return self._balance

def bank_account_example():
    account = ThreadSafeBankAccount(1000)
    
    def depositor():
        for _ in range(5):
            account.deposit(100)
            time.sleep(0.1)
    
    def withdrawer():
        for _ in range(5):
            account.withdraw(50)
            time.sleep(0.1)
    
    depositor_thread = threading.Thread(target=depositor)
    withdrawer_thread = threading.Thread(target=withdrawer)
    
    depositor_thread.start()
    withdrawer_thread.start()
    
    depositor_thread.join()
    withdrawer_thread.join()
    
    print(f"Final balance: {account.get_balance()}")

bank_account_example()

# 2. Multithreaded web scraper
print("\nExercise 2: Multithreaded Web Scraper")
def multithreaded_web_scraper():
    import urllib.request
    
    def fetch_url(url):
        try:
            with urllib.request.urlopen(url) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"Error: {e}"
    
    urls = [
        "http://httpbin.org/json",
        "http://httpbin.org/uuid",
        "http://httpbin.org/ip",
        "http://httpbin.org/user-agent"
    ]
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(fetch_url, url) for url in urls]
        results = [future.result() for future in futures]
    
    print("Web scraper results:")
    for i, result in enumerate(results):
        print(f"  URL {i+1}: {result[:50]}...")

multithreaded_web_scraper()

# 3. Thread pool for image processing
print("\nExercise 3: Thread Pool for Image Processing")
def image_processing_thread_pool():
    def process_image(image_id):
        time.sleep(0.1)  # Simulate image processing
        return f"Processed image {image_id}"
    
    image_ids = list(range(20))
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_image, img_id) for img_id in image_ids]
        results = [future.result() for future in futures]
    
    print("Image processing results:")
    for result in results:
        print(f"  {result}")

image_processing_thread_pool()

# 4. Producer-consumer pattern
print("\nExercise 4: Producer-Consumer Pattern")
def producer_consumer_pattern():
    import queue
    
    q = queue.Queue(maxsize=5)
    
    def producer():
        for i in range(10):
            q.put(f"item-{i}")
            print(f"Produced: item-{i}")
            time.sleep(0.1)
        q.put(None)  # Signal end
    
    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            print(f"Consumed: {item}")
            time.sleep(0.1)
            q.task_done()
    
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()

producer_consumer_pattern()

# 5. Thread-safe cache
print("\nExercise 5: Thread-safe Cache")
class ThreadSafeCache:
    def __init__(self, max_size=100):
        self._cache = {}
        self._max_size = max_size
        self._lock = threading.RLock()
    
    def get(self, key):
        with self._lock:
            return self._cache.get(key)
    
    def set(self, key, value):
        with self._lock:
            if len(self._cache) >= self._max_size:
                # Remove oldest item
                oldest_key = next(iter(self._cache))
                del self._cache[oldest_key]
            self._cache[key] = value
    
    def size(self):
        with self._lock:
            return len(self._cache)

def thread_safe_cache_example():
    cache = ThreadSafeCache(max_size=5)
    
    def cache_worker(worker_id):
        for i in range(10):
            key = f"key-{worker_id}-{i}"
            value = f"value-{worker_id}-{i}"
            cache.set(key, value)
            time.sleep(0.1)
    
    threads = []
    for i in range(3):
        thread = threading.Thread(target=cache_worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Cache size: {cache.size()}")

thread_safe_cache_example()

print("\n🎉 Congratulations! You've completed Lesson 27!")
print("Next: Lesson 28 - Multiprocessing")
