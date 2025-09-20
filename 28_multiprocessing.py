# Lesson 28: Multiprocessing

"""
This lesson covers:
- What is multiprocessing
- multiprocessing module
- Process creation and management
- Process communication
- Shared memory
- Process pools
- Inter-process communication (IPC)
- Process synchronization
- When to use multiprocessing vs threading
- Practical multiprocessing examples
"""

# 1. What is Multiprocessing
print("=== What is Multiprocessing ===")

# Multiprocessing allows multiple processes to run concurrently
# Each process has its own memory space and Python interpreter

import multiprocessing
import time
import os

# Simple process example
def worker_process(name, delay):
    print(f"Process {name} (PID: {os.getpid()}) starting")
    time.sleep(delay)
    print(f"Process {name} (PID: {os.getpid()}) completed")

# Create and start processes
process1 = multiprocessing.Process(target=worker_process, args=("A", 1))
process2 = multiprocessing.Process(target=worker_process, args=("B", 2))

print(f"Main process PID: {os.getpid()}")
print("Starting processes...")
process1.start()
process2.start()

# Wait for processes to complete
process1.join()
process2.join()
print("All processes completed")

# 2. multiprocessing Module
print("\n=== multiprocessing Module ===")

# Process class
class CustomProcess(multiprocessing.Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        print(f"Custom process {self.name} (PID: {os.getpid()}) starting")
        time.sleep(self.delay)
        print(f"Custom process {self.name} (PID: {os.getpid()}) completed")

# Create and start custom processes
custom_process1 = CustomProcess("Custom-A", 1)
custom_process2 = CustomProcess("Custom-B", 1.5)

custom_process1.start()
custom_process2.start()

custom_process1.join()
custom_process2.join()

# 3. Process Creation and Management
print("\n=== Process Creation and Management ===")

# Process attributes
def process_info():
    current_process = multiprocessing.current_process()
    print(f"Current process: {current_process.name}")
    print(f"Process ID: {current_process.pid}")
    print(f"Is alive: {current_process.is_alive()}")
    print(f"Exit code: {current_process.exitcode}")

# Main process info
process_info()

# Create new process
new_process = multiprocessing.Process(target=process_info, name="InfoProcess")
new_process.start()
new_process.join()

# Process enumeration
print(f"Active processes: {multiprocessing.active_children()}")
print(f"CPU count: {multiprocessing.cpu_count()}")

# 4. Process Communication
print("\n=== Process Communication ===")

# Queue for inter-process communication
def queue_example():
    queue = multiprocessing.Queue()
    
    def producer(queue):
        for i in range(5):
            queue.put(f"item-{i}")
            print(f"Producer put: item-{i}")
            time.sleep(0.1)
        queue.put(None)  # Signal end
    
    def consumer(queue):
        while True:
            item = queue.get()
            if item is None:
                break
            print(f"Consumer got: {item}")
            time.sleep(0.1)
    
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
    
    producer_process.start()
    consumer_process.start()
    
    producer_process.join()
    consumer_process.join()

queue_example()

# Pipe for bidirectional communication
def pipe_example():
    parent_conn, child_conn = multiprocessing.Pipe()
    
    def child_process(conn):
        for i in range(3):
            message = f"Hello from child {i}"
            conn.send(message)
            print(f"Child sent: {message}")
            time.sleep(0.1)
        conn.close()
    
    child = multiprocessing.Process(target=child_process, args=(child_conn,))
    child.start()
    
    while True:
        try:
            message = parent_conn.recv()
            print(f"Parent received: {message}")
        except EOFError:
            break
    
    child.join()
    parent_conn.close()

pipe_example()

# 5. Shared Memory
print("\n=== Shared Memory ===")

# Value for shared data
def value_example():
    shared_value = multiprocessing.Value('i', 0)  # 'i' for integer
    
    def incrementer(value):
        for _ in range(1000):
            with value.get_lock():
                value.value += 1
    
    def decrementer(value):
        for _ in range(1000):
            with value.get_lock():
                value.value -= 1
    
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=incrementer, args=(shared_value,))
        processes.append(p)
        p.start()
    
    for _ in range(5):
        p = multiprocessing.Process(target=decrementer, args=(shared_value,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"Final shared value: {shared_value.value}")

value_example()

# Array for shared arrays
def array_example():
    shared_array = multiprocessing.Array('i', [0, 0, 0, 0, 0])  # 'i' for integer
    
    def array_worker(array, index):
        for _ in range(1000):
            with array.get_lock():
                array[index] += 1
    
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=array_worker, args=(shared_array, i))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"Final shared array: {list(shared_array)}")

array_example()

# 6. Process Pools
print("\n=== Process Pools ===")

# ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def process_pool_example():
    def worker_task(task_id):
        print(f"Worker {task_id} (PID: {os.getpid()}) starting")
        time.sleep(1)
        print(f"Worker {task_id} (PID: {os.getpid()}) completed")
        return f"Result from worker {task_id}"
    
    # Create process pool
    with ProcessPoolExecutor(max_workers=3) as executor:
        # Submit tasks
        futures = [executor.submit(worker_task, i) for i in range(5)]
        
        # Get results
        results = [future.result() for future in futures]
        print(f"Results: {results}")

process_pool_example()

# Process pool with map
def process_pool_map_example():
    def process_item(item):
        print(f"Processing item {item} (PID: {os.getpid()})")
        time.sleep(0.1)
        return f"Processed {item}"
    
    items = [1, 2, 3, 4, 5]
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_item, items))
        print(f"Map results: {results}")

process_pool_map_example()

# 7. Inter-process Communication (IPC)
print("\n=== Inter-process Communication (IPC) ===")

# Manager for shared objects
def manager_example():
    manager = multiprocessing.Manager()
    shared_dict = manager.dict()
    shared_list = manager.list()
    
    def worker(worker_id, shared_dict, shared_list):
        shared_dict[f"worker_{worker_id}"] = f"data_{worker_id}"
        shared_list.append(worker_id)
        print(f"Worker {worker_id} updated shared objects")
    
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i, shared_dict, shared_list))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"Shared dict: {dict(shared_dict)}")
    print(f"Shared list: {list(shared_list)}")

manager_example()

# Event for process synchronization
def event_example():
    event = multiprocessing.Event()
    
    def waiter():
        print("Waiter waiting for event")
        event.wait()
        print("Waiter received event")
    
    def setter():
        time.sleep(2)
        print("Setter setting event")
        event.set()
    
    waiter_process = multiprocessing.Process(target=waiter)
    setter_process = multiprocessing.Process(target=setter)
    
    waiter_process.start()
    setter_process.start()
    
    waiter_process.join()
    setter_process.join()

event_example()

# 8. Process Synchronization
print("\n=== Process Synchronization ===")

# Lock for process synchronization
def lock_example():
    lock = multiprocessing.Lock()
    
    def critical_section(process_id):
        print(f"Process {process_id} waiting for lock")
        with lock:
            print(f"Process {process_id} acquired lock")
            time.sleep(0.1)
            print(f"Process {process_id} releasing lock")
    
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=critical_section, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

lock_example()

# Semaphore for process synchronization
def semaphore_example():
    semaphore = multiprocessing.Semaphore(2)  # Allow 2 processes at a time
    
    def worker(worker_id):
        print(f"Worker {worker_id} waiting for semaphore")
        with semaphore:
            print(f"Worker {worker_id} acquired semaphore")
            time.sleep(1)
            print(f"Worker {worker_id} releasing semaphore")
    
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

semaphore_example()

# 9. When to Use Multiprocessing vs Threading
print("\n=== When to Use Multiprocessing vs Threading ===")

# Multiprocessing is good for:
# - CPU-bound tasks
# - True parallelism
# - Isolation between processes
# - Avoiding GIL limitations

# Threading is good for:
# - I/O-bound tasks
# - Shared memory access
# - Lower overhead
# - Simpler communication

def multiprocessing_vs_threading_example():
    # CPU-bound task
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
        
        # Multiprocessing execution
        start_time = time.time()
        
        with ProcessPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(cpu_bound_task, 1000000) for _ in range(4)]
            results = [future.result() for future in futures]
        
        multiprocessing_time = time.time() - start_time
        print(f"Multiprocessing time: {multiprocessing_time:.2f}s")
        print(f"Performance ratio: {sequential_time/multiprocessing_time:.2f}")
    
    test_cpu_bound()

multiprocessing_vs_threading_example()

# 10. Practical Multiprocessing Examples
print("\n=== Practical Multiprocessing Examples ===")

# Example 1: CPU-intensive computation
def cpu_intensive_example():
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    def compute_fibonacci(n):
        print(f"Computing fibonacci({n}) (PID: {os.getpid()})")
        return fibonacci(n)
    
    numbers = [30, 31, 32, 33]
    
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(compute_fibonacci, n) for n in numbers]
        results = [future.result() for future in futures]
    
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing time: {multiprocessing_time:.2f}s")
    print(f"Results: {results}")

cpu_intensive_example()

# Example 2: Data processing pipeline
def data_processing_pipeline():
    def process_data_chunk(chunk):
        print(f"Processing chunk {chunk} (PID: {os.getpid()})")
        time.sleep(0.1)  # Simulate processing
        return f"Processed chunk {chunk}"
    
    data_chunks = list(range(10))
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(process_data_chunk, chunk) for chunk in data_chunks]
        results = [future.result() for future in futures]
    
    print("Data processing results:")
    for result in results:
        print(f"  {result}")

data_processing_pipeline()

# Example 3: Parallel file processing
def parallel_file_processing():
    def process_file(filename):
        print(f"Processing {filename} (PID: {os.getpid()})")
        time.sleep(0.1)  # Simulate file processing
        return f"Processed {filename}"
    
    filenames = [f"file{i}.txt" for i in range(15)]
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_file, filename) for filename in filenames]
        results = [future.result() for future in futures]
    
    print("File processing results:")
    for result in results:
        print(f"  {result}")

parallel_file_processing()

# 11. Process Monitoring and Debugging
print("\n=== Process Monitoring and Debugging ===")

# Process monitoring
def process_monitoring_example():
    def worker():
        print(f"Worker starting (PID: {os.getpid()})")
        time.sleep(2)
        print(f"Worker completed (PID: {os.getpid()})")
    
    def monitor_processes():
        while True:
            active_processes = multiprocessing.active_children()
            print(f"Active processes: {len(active_processes)}")
            for p in active_processes:
                print(f"  Process {p.name} (PID: {p.pid})")
            time.sleep(0.5)
    
    monitor_process = multiprocessing.Process(target=monitor_processes, daemon=True)
    worker_process = multiprocessing.Process(target=worker)
    
    monitor_process.start()
    worker_process.start()
    
    worker_process.join()

process_monitoring_example()

# Process debugging
def process_debugging_example():
    def worker_with_debug(worker_id):
        print(f"Worker {worker_id} starting (PID: {os.getpid()})")
        try:
            time.sleep(0.1)
            if worker_id == 2:
                raise Exception(f"Error in worker {worker_id}")
            print(f"Worker {worker_id} completed successfully")
        except Exception as e:
            print(f"Worker {worker_id} failed: {e}")
    
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker_with_debug, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

process_debugging_example()

# 12. Advanced Multiprocessing Patterns
print("\n=== Advanced Multiprocessing Patterns ===")

# Pattern 1: Producer-Consumer with Processes
def producer_consumer_processes():
    queue = multiprocessing.Queue()
    
    def producer(queue):
        for i in range(10):
            queue.put(f"item-{i}")
            print(f"Producer put: item-{i}")
            time.sleep(0.1)
        queue.put(None)  # Signal end
    
    def consumer(queue):
        while True:
            item = queue.get()
            if item is None:
                break
            print(f"Consumer got: {item}")
            time.sleep(0.1)
    
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
    
    producer_process.start()
    consumer_process.start()
    
    producer_process.join()
    consumer_process.join()

producer_consumer_processes()

# Pattern 2: Map-Reduce with Processes
def map_reduce_processes():
    def mapper(data):
        return [x * 2 for x in data]
    
    def reducer(results):
        return sum(results)
    
    # Split data into chunks
    data = list(range(100))
    chunk_size = 25
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Map phase
    with ProcessPoolExecutor(max_workers=4) as executor:
        mapped_results = list(executor.map(mapper, chunks))
    
    # Reduce phase
    flattened_results = [item for sublist in mapped_results for item in sublist]
    final_result = reducer(flattened_results)
    
    print(f"Map-reduce result: {final_result}")

map_reduce_processes()

# Pattern 3: Pipeline with Processes
def pipeline_processes():
    def stage1(data):
        return [x + 1 for x in data]
    
    def stage2(data):
        return [x * 2 for x in data]
    
    def stage3(data):
        return [x - 1 for x in data]
    
    data = list(range(10))
    
    # Process through pipeline stages
    with ProcessPoolExecutor(max_workers=3) as executor:
        stage1_result = executor.submit(stage1, data).result()
        stage2_result = executor.submit(stage2, stage1_result).result()
        stage3_result = executor.submit(stage3, stage2_result).result()
    
    print(f"Pipeline result: {stage3_result}")

pipeline_processes()

# Exercises:
"""
1. Create a multiprocessing-based prime number finder
2. Write a parallel image processing system
3. Create a multiprocessing web scraper
4. Write a distributed computing simulation
5. Create a multiprocessing-based data analysis pipeline
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Prime number finder
print("Exercise 1: Prime Number Finder")
def prime_number_finder():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def find_primes_in_range(start, end):
        primes = []
        for i in range(start, end):
            if is_prime(i):
                primes.append(i)
        return primes
    
    # Split range into chunks
    start, end = 2, 1000
    chunk_size = 100
    ranges = [(i, min(i + chunk_size, end)) for i in range(start, end, chunk_size)]
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(find_primes_in_range, start, end) for start, end in ranges]
        results = [future.result() for future in futures]
    
    all_primes = [prime for sublist in results for prime in sublist]
    print(f"Found {len(all_primes)} primes in range {start}-{end}")
    print(f"First 10 primes: {all_primes[:10]}")

prime_number_finder()

# 2. Parallel image processing
print("\nExercise 2: Parallel Image Processing")
def parallel_image_processing():
    def process_image(image_id):
        print(f"Processing image {image_id} (PID: {os.getpid()})")
        time.sleep(0.1)  # Simulate image processing
        return f"Processed image {image_id}"
    
    image_ids = list(range(20))
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_image, img_id) for img_id in image_ids]
        results = [future.result() for future in futures]
    
    print("Image processing results:")
    for result in results:
        print(f"  {result}")

parallel_image_processing()

# 3. Multiprocessing web scraper
print("\nExercise 3: Multiprocessing Web Scraper")
def multiprocessing_web_scraper():
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
        "http://httpbin.org/user-agent",
        "http://httpbin.org/headers"
    ]
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_url, url) for url in urls]
        results = [future.result() for future in futures]
    
    print("Web scraper results:")
    for i, result in enumerate(results):
        print(f"  URL {i+1}: {result[:50]}...")

multiprocessing_web_scraper()

# 4. Distributed computing simulation
print("\nExercise 4: Distributed Computing Simulation")
def distributed_computing_simulation():
    def compute_task(task_id, data):
        print(f"Computing task {task_id} (PID: {os.getpid()})")
        time.sleep(0.1)  # Simulate computation
        return f"Task {task_id} result: {sum(data)}"
    
    # Create tasks with data
    tasks = [(i, list(range(i*10, (i+1)*10))) for i in range(10)]
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(compute_task, task_id, data) for task_id, data in tasks]
        results = [future.result() for future in futures]
    
    print("Distributed computing results:")
    for result in results:
        print(f"  {result}")

distributed_computing_simulation()

# 5. Data analysis pipeline
print("\nExercise 5: Data Analysis Pipeline")
def data_analysis_pipeline():
    def load_data(data_id):
        print(f"Loading data {data_id} (PID: {os.getpid()})")
        time.sleep(0.1)
        return list(range(data_id*10, (data_id+1)*10))
    
    def analyze_data(data):
        print(f"Analyzing data (PID: {os.getpid()})")
        time.sleep(0.1)
        return {
            'sum': sum(data),
            'mean': sum(data) / len(data),
            'max': max(data),
            'min': min(data)
        }
    
    def aggregate_results(results):
        print(f"Aggregating results (PID: {os.getpid()})")
        time.sleep(0.1)
        return {
            'total_sum': sum(r['sum'] for r in results),
            'avg_mean': sum(r['mean'] for r in results) / len(results),
            'global_max': max(r['max'] for r in results),
            'global_min': min(r['min'] for r in results)
        }
    
    # Load data
    data_ids = list(range(5))
    with ProcessPoolExecutor(max_workers=3) as executor:
        data_futures = [executor.submit(load_data, data_id) for data_id in data_ids]
        datasets = [future.result() for future in data_futures]
    
    # Analyze data
    with ProcessPoolExecutor(max_workers=3) as executor:
        analysis_futures = [executor.submit(analyze_data, data) for data in datasets]
        analyses = [future.result() for future in analysis_futures]
    
    # Aggregate results
    final_result = aggregate_results(analyses)
    
    print("Data analysis pipeline results:")
    print(f"  Total sum: {final_result['total_sum']}")
    print(f"  Average mean: {final_result['avg_mean']:.2f}")
    print(f"  Global max: {final_result['global_max']}")
    print(f"  Global min: {final_result['global_min']}")

data_analysis_pipeline()

print("\n🎉 Congratulations! You've completed Lesson 28!")
print("Next: Lesson 29 - Networking")
