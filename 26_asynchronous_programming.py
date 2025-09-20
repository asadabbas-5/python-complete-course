# Lesson 26: Asynchronous Programming

"""
This lesson covers:
- What is asynchronous programming
- async/await syntax
- asyncio module
- Coroutines and tasks
- Event loops
- Asynchronous I/O operations
- Error handling in async code
- Practical async examples
"""

# 1. What is Asynchronous Programming
print("=== What is Asynchronous Programming ===")

# Asynchronous programming allows multiple operations to run concurrently
# without blocking the main thread

import asyncio
import time

# Synchronous function
def sync_function():
    print("Starting sync function")
    time.sleep(1)  # Blocking operation
    print("Sync function completed")
    return "sync result"

# Asynchronous function
async def async_function():
    print("Starting async function")
    await asyncio.sleep(1)  # Non-blocking operation
    print("Async function completed")
    return "async result"

# Compare synchronous vs asynchronous
print("Synchronous execution:")
start_time = time.time()
result1 = sync_function()
result2 = sync_function()
sync_time = time.time() - start_time
print(f"Sync time: {sync_time:.2f}s")

print("\nAsynchronous execution:")
start_time = time.time()
result1 = asyncio.run(async_function())
result2 = asyncio.run(async_function())
async_time = time.time() - start_time
print(f"Async time: {async_time:.2f}s")

# 2. async/await Syntax
print("\n=== async/await Syntax ===")

# Basic async function
async def greet(name):
    await asyncio.sleep(0.1)  # Simulate async operation
    return f"Hello, {name}!"

# Async function that calls other async functions
async def main():
    # Sequential execution
    result1 = await greet("Alice")
    result2 = await greet("Bob")
    print(f"Sequential: {result1}, {result2}")
    
    # Concurrent execution
    task1 = asyncio.create_task(greet("Charlie"))
    task2 = asyncio.create_task(greet("Diana"))
    
    result1 = await task1
    result2 = await task2
    print(f"Concurrent: {result1}, {result2}")

# Run the async function
asyncio.run(main())

# 3. asyncio Module
print("\n=== asyncio Module ===")

# asyncio.run() - Run async function
async def simple_async():
    print("Running simple async function")
    await asyncio.sleep(0.1)
    return "done"

result = asyncio.run(simple_async())
print(f"Result: {result}")

# asyncio.create_task() - Create task
async def task_example():
    async def worker(name, delay):
        print(f"Worker {name} starting")
        await asyncio.sleep(delay)
        print(f"Worker {name} completed")
        return f"Worker {name} result"
    
    # Create tasks
    task1 = asyncio.create_task(worker("A", 0.1))
    task2 = asyncio.create_task(worker("B", 0.2))
    task3 = asyncio.create_task(worker("C", 0.15))
    
    # Wait for all tasks
    results = await asyncio.gather(task1, task2, task3)
    print(f"All results: {results}")

asyncio.run(task_example())

# 4. Coroutines and Tasks
print("\n=== Coroutines and Tasks ===")

# Coroutine function
async def coroutine_function():
    print("Coroutine started")
    await asyncio.sleep(0.1)
    print("Coroutine completed")
    return "coroutine result"

# Create coroutine
coro = coroutine_function()
print(f"Coroutine object: {coro}")

# Run coroutine
result = asyncio.run(coro)
print(f"Coroutine result: {result}")

# Task from coroutine
async def task_example():
    coro = coroutine_function()
    task = asyncio.create_task(coro)
    print(f"Task object: {task}")
    
    result = await task
    print(f"Task result: {result}")

asyncio.run(task_example())

# 5. Event Loops
print("\n=== Event Loops ===")

# Get current event loop
async def event_loop_example():
    loop = asyncio.get_running_loop()
    print(f"Current event loop: {loop}")
    
    # Schedule callback
    loop.call_soon(print, "Callback executed")
    
    # Schedule delayed callback
    loop.call_later(0.1, print, "Delayed callback executed")
    
    await asyncio.sleep(0.2)

asyncio.run(event_loop_example())

# Custom event loop
async def custom_loop_example():
    # Create custom event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # Run coroutine in custom loop
        result = await coroutine_function()
        print(f"Custom loop result: {result}")
    finally:
        loop.close()

asyncio.run(custom_loop_example())

# 6. Asynchronous I/O Operations
print("\n=== Asynchronous I/O Operations ===")

# Async file operations
async def async_file_operations():
    # Write to file
    with open("async_test.txt", "w") as f:
        f.write("Hello, Async World!")
    
    # Read from file
    with open("async_test.txt", "r") as f:
        content = f.read()
        print(f"File content: {content}")
    
    # Simulate async file operation
    await asyncio.sleep(0.1)
    print("File operation completed")

asyncio.run(async_file_operations())

# Async network operations
async def async_network_example():
    import aiohttp
    
    async def fetch_url(session, url):
        try:
            async with session.get(url) as response:
                return await response.text()
        except Exception as e:
            return f"Error: {e}"
    
    # This would work with aiohttp installed
    # async with aiohttp.ClientSession() as session:
    #     urls = ["http://httpbin.org/json", "http://httpbin.org/uuid"]
    #     tasks = [fetch_url(session, url) for url in urls]
    #     results = await asyncio.gather(*tasks)
    #     print(f"Network results: {results}")
    
    print("Network example (aiohttp not installed)")

asyncio.run(async_network_example())

# 7. Error Handling in Async Code
print("\n=== Error Handling in Async Code ===")

# Async function with error handling
async def async_error_handling():
    async def risky_operation(value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        await asyncio.sleep(0.1)
        return value * 2
    
    # Handle errors in async function
    try:
        result = await risky_operation(5)
        print(f"Success: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Handle errors in tasks
    tasks = [
        asyncio.create_task(risky_operation(10)),
        asyncio.create_task(risky_operation(-5)),
        asyncio.create_task(risky_operation(20))
    ]
    
    # Wait for all tasks, return exceptions
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Task results: {results}")

asyncio.run(async_error_handling())

# 8. Practical Async Examples
print("\n=== Practical Async Examples ===")

# Example 1: Async Web Scraper
async def async_web_scraper():
    import urllib.request
    import urllib.parse
    
    async def fetch_page(url):
        # Simulate async network request
        await asyncio.sleep(0.1)
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
    
    # Fetch pages concurrently
    tasks = [fetch_page(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    print("Web scraper results:")
    for i, result in enumerate(results):
        print(f"URL {i+1}: {result[:50]}...")

asyncio.run(async_web_scraper())

# Example 2: Async Database Operations
async def async_database_example():
    # Simulate async database operations
    async def db_query(query):
        await asyncio.sleep(0.1)  # Simulate database delay
        return f"Result for: {query}"
    
    # Execute multiple queries concurrently
    queries = ["SELECT * FROM users", "SELECT * FROM orders", "SELECT * FROM products"]
    tasks = [db_query(query) for query in queries]
    results = await asyncio.gather(*tasks)
    
    print("Database results:")
    for result in results:
        print(f"  {result}")

asyncio.run(async_database_example())

# Example 3: Async File Processing
async def async_file_processing():
    # Simulate async file processing
    async def process_file(filename):
        await asyncio.sleep(0.1)  # Simulate processing time
        return f"Processed {filename}"
    
    # Process multiple files concurrently
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = [process_file(filename) for filename in filenames]
    results = await asyncio.gather(*tasks)
    
    print("File processing results:")
    for result in results:
        print(f"  {result}")

asyncio.run(async_file_processing())

# 9. Async Patterns
print("\n=== Async Patterns ===")

# Pattern 1: Producer-Consumer
async def producer_consumer_pattern():
    import asyncio
    
    async def producer(queue):
        for i in range(5):
            await asyncio.sleep(0.1)
            await queue.put(f"Item {i}")
            print(f"Produced: Item {i}")
        await queue.put(None)  # Signal end
    
    async def consumer(queue):
        while True:
            item = await queue.get()
            if item is None:
                break
            await asyncio.sleep(0.1)
            print(f"Consumed: {item}")
            queue.task_done()
    
    # Create queue and run producer-consumer
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )

asyncio.run(producer_consumer_pattern())

# Pattern 2: Async Context Manager
class AsyncContextManager:
    async def __aenter__(self):
        print("Entering async context")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting async context")
        await asyncio.sleep(0.1)
        return False

async def async_context_example():
    async with AsyncContextManager() as cm:
        print("Inside async context")
        await asyncio.sleep(0.1)

asyncio.run(async_context_example())

# Pattern 3: Async Generator
async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i

async def async_generator_example():
    async for value in async_generator():
        print(f"Generated: {value}")

asyncio.run(async_generator_example())

# 10. Async Best Practices
print("\n=== Async Best Practices ===")

# Best Practice 1: Use asyncio.gather() for concurrent operations
async def best_practice_gather():
    async def worker(name, delay):
        await asyncio.sleep(delay)
        return f"Worker {name} completed"
    
    # Good: Use gather for concurrent operations
    results = await asyncio.gather(
        worker("A", 0.1),
        worker("B", 0.2),
        worker("C", 0.15)
    )
    print(f"Gather results: {results}")

asyncio.run(best_practice_gather())

# Best Practice 2: Handle exceptions properly
async def best_practice_exceptions():
    async def risky_task(value):
        if value < 0:
            raise ValueError("Negative value")
        await asyncio.sleep(0.1)
        return value * 2
    
    # Handle exceptions in gather
    tasks = [
        asyncio.create_task(risky_task(5)),
        asyncio.create_task(risky_task(-3)),
        asyncio.create_task(risky_task(10))
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Exception handling results: {results}")

asyncio.run(best_practice_exceptions())

# Best Practice 3: Use asyncio.create_task() for fire-and-forget
async def best_practice_tasks():
    async def background_task():
        await asyncio.sleep(0.1)
        print("Background task completed")
    
    # Create task for background work
    task = asyncio.create_task(background_task())
    
    # Do other work
    await asyncio.sleep(0.05)
    print("Main work completed")
    
    # Wait for background task
    await task

asyncio.run(best_practice_tasks())

# 11. Async Performance Considerations
print("\n=== Async Performance Considerations ===")

# Compare sync vs async performance
def sync_operations():
    start_time = time.time()
    for i in range(5):
        time.sleep(0.1)
    return time.time() - start_time

async def async_operations():
    start_time = time.time()
    tasks = [asyncio.sleep(0.1) for _ in range(5)]
    await asyncio.gather(*tasks)
    return time.time() - start_time

# Test performance
sync_time = sync_operations()
async_time = asyncio.run(async_operations())

print(f"Sync operations time: {sync_time:.2f}s")
print(f"Async operations time: {async_time:.2f}s")
print(f"Performance improvement: {sync_time/async_time:.2f}x")

# 12. Real-world Async Examples
print("\n=== Real-world Async Examples ===")

# Example 1: Async Web Server
async def async_web_server():
    from aiohttp import web
    
    async def handle_request(request):
        await asyncio.sleep(0.1)  # Simulate processing
        return web.Response(text="Hello, Async World!")
    
    app = web.Application()
    app.router.add_get('/', handle_request)
    
    # This would start the server
    # web.run_app(app, host='localhost', port=8080)
    print("Async web server example (aiohttp not installed)")

asyncio.run(async_web_server())

# Example 2: Async Data Processing Pipeline
async def async_data_pipeline():
    async def fetch_data(source):
        await asyncio.sleep(0.1)
        return f"Data from {source}"
    
    async def process_data(data):
        await asyncio.sleep(0.1)
        return f"Processed: {data}"
    
    async def save_data(data):
        await asyncio.sleep(0.1)
        return f"Saved: {data}"
    
    # Process data pipeline
    sources = ["API", "Database", "File"]
    
    # Fetch data concurrently
    raw_data = await asyncio.gather(*[fetch_data(source) for source in sources])
    
    # Process data concurrently
    processed_data = await asyncio.gather(*[process_data(data) for data in raw_data])
    
    # Save data concurrently
    saved_data = await asyncio.gather(*[save_data(data) for data in processed_data])
    
    print("Data pipeline results:")
    for result in saved_data:
        print(f"  {result}")

asyncio.run(async_data_pipeline())

# Example 3: Async Monitoring System
async def async_monitoring_system():
    async def monitor_service(service_name):
        while True:
            await asyncio.sleep(0.1)
            print(f"Monitoring {service_name}")
            # Simulate monitoring logic
            await asyncio.sleep(0.1)
    
    # Start monitoring tasks
    services = ["Web Server", "Database", "Cache", "Queue"]
    tasks = [asyncio.create_task(monitor_service(service)) for service in services]
    
    # Run for a short time
    await asyncio.sleep(0.5)
    
    # Cancel all tasks
    for task in tasks:
        task.cancel()
    
    print("Monitoring system stopped")

asyncio.run(async_monitoring_system())

# Cleanup
import os
if os.path.exists("async_test.txt"):
    os.remove("async_test.txt")

# Exercises:
"""
1. Create an async function that simulates downloading multiple files
2. Write an async function that processes a list of URLs concurrently
3. Create an async context manager for database connections
4. Write an async generator that yields data from a streaming source
5. Create an async function that handles rate limiting
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Async file downloader
print("Exercise 1: Async File Downloader")
async def async_file_downloader():
    async def download_file(filename, size):
        await asyncio.sleep(size * 0.01)  # Simulate download time
        return f"Downloaded {filename} ({size}MB)"
    
    files = [
        ("file1.txt", 10),
        ("file2.txt", 5),
        ("file3.txt", 15),
        ("file4.txt", 8)
    ]
    
    tasks = [download_file(filename, size) for filename, size in files]
    results = await asyncio.gather(*tasks)
    
    print("Download results:")
    for result in results:
        print(f"  {result}")

asyncio.run(async_file_downloader())

# 2. Async URL processor
print("\nExercise 2: Async URL Processor")
async def async_url_processor():
    async def process_url(url):
        await asyncio.sleep(0.1)
        return f"Processed {url}"
    
    urls = [
        "http://example.com",
        "http://google.com",
        "http://github.com"
    ]
    
    tasks = [process_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    print("URL processing results:")
    for result in results:
        print(f"  {result}")

asyncio.run(async_url_processor())

# 3. Async database context manager
print("\nExercise 3: Async Database Context Manager")
class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("Connecting to database")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        await asyncio.sleep(0.1)
        return False
    
    async def query(self, sql):
        await asyncio.sleep(0.1)
        return f"Result for: {sql}"

async def async_database_example():
    async with AsyncDatabaseConnection() as db:
        result = await db.query("SELECT * FROM users")
        print(f"Database result: {result}")

asyncio.run(async_database_example())

# 4. Async generator
print("\nExercise 4: Async Generator")
async def async_data_stream():
    for i in range(5):
        await asyncio.sleep(0.1)
        yield f"Data chunk {i}"

async def async_generator_example():
    async for chunk in async_data_stream():
        print(f"Received: {chunk}")

asyncio.run(async_generator_example())

# 5. Async rate limiter
print("\nExercise 5: Async Rate Limiter")
class AsyncRateLimiter:
    def __init__(self, max_requests=5, time_window=1):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
    
    async def acquire(self):
        now = time.time()
        
        # Remove old requests
        self.requests = [req_time for req_time in self.requests 
                        if now - req_time < self.time_window]
        
        if len(self.requests) >= self.max_requests:
            await asyncio.sleep(self.time_window - (now - self.requests[0]))
            return await self.acquire()
        
        self.requests.append(now)

async def async_rate_limiter_example():
    rate_limiter = AsyncRateLimiter(max_requests=2, time_window=1)
    
    async def make_request(request_id):
        await rate_limiter.acquire()
        print(f"Request {request_id} made")
    
    tasks = [make_request(i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(async_rate_limiter_example())

print("\n🎉 Congratulations! You've completed Lesson 26!")
print("Next: Lesson 27 - Multithreading")
