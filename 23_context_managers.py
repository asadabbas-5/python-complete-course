# Lesson 23: Context Managers

"""
This lesson covers:
- What are context managers
- The 'with' statement
- Built-in context managers
- Creating custom context managers
- Context manager protocols
- Contextlib utilities
- Exception handling in context managers
- Practical context manager examples
"""

# 1. What are Context Managers
print("=== What are Context Managers ===")

# Context managers are objects that define methods to be used with the 'with' statement
# They ensure proper setup and cleanup of resources

# Basic example with file handling
try:
    with open("sample.txt", "w") as file:
        file.write("Hello, World!")
    print("File written successfully")
except FileNotFoundError:
    print("Could not create file")

# The 'with' statement ensures the file is properly closed
# even if an exception occurs

# 2. The 'with' Statement
print("\n=== The 'with' Statement ===")

# The 'with' statement calls __enter__ and __exit__ methods
# It's equivalent to:
# manager = context_manager()
# manager.__enter__()
# try:
#     # code block
# finally:
#     manager.__exit__()

# Multiple context managers
with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Content for file 1")
    f2.write("Content for file 2")

print("Multiple files written")

# 3. Built-in Context Managers
print("\n=== Built-in Context Managers ===")

# File handling
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# Threading locks
import threading

lock = threading.Lock()
with lock:
    print("Critical section executed")

# Decimal context
from decimal import Decimal, getcontext

with getcontext() as ctx:
    ctx.prec = 2
    result = Decimal('1') / Decimal('3')
    print(f"Decimal result: {result}")

# 4. Creating Custom Context Managers
print("\n=== Creating Custom Context Managers ===")

# Method 1: Using class with __enter__ and __exit__
class FileManager:
    """Custom file manager context manager"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        
        return False  # Don't suppress exceptions

# Use custom context manager
with FileManager("custom.txt", "w") as file:
    file.write("Custom context manager")

# Method 2: Using contextlib.contextmanager decorator
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """File manager using contextmanager decorator"""
    print(f"Opening file: {filename}")
    file = open(filename, mode)
    try:
        yield file
    finally:
        print(f"Closing file: {filename}")
        file.close()

# Use contextmanager decorator
with file_manager("decorator.txt", "w") as file:
    file.write("Context manager with decorator")

# 5. Context Manager Protocols
print("\n=== Context Manager Protocols ===")

class DatabaseConnection:
    """Database connection context manager"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to database: {self.connection_string}")
        # Simulate database connection
        self.connection = f"Connection to {self.connection_string}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        self.connection = None
        
        if exc_type:
            print(f"Database error: {exc_type.__name__}: {exc_val}")
            # Return True to suppress the exception
            return True
        
        return False

# Use database context manager
with DatabaseConnection("localhost:5432") as conn:
    print(f"Using connection: {conn}")
    # Simulate database operation
    print("Executing query...")

# Test with exception
try:
    with DatabaseConnection("localhost:5432") as conn:
        print(f"Using connection: {conn}")
        raise ValueError("Database error")
except ValueError as e:
    print(f"Caught exception: {e}")

# 6. Contextlib Utilities
print("\n=== Contextlib Utilities ===")

# contextlib.closing
from contextlib import closing
from urllib.request import urlopen

# Use closing for objects with close() method
with closing(urlopen('http://httpbin.org/json')) as response:
    print(f"Response status: {response.status}")

# contextlib.suppress
from contextlib import suppress
import os

# Suppress specific exceptions
with suppress(FileNotFoundError):
    os.remove("nonexistent.txt")
    print("File removed")

# contextlib.redirect_stdout
from contextlib import redirect_stdout
import io

# Redirect stdout to a string
output = io.StringIO()
with redirect_stdout(output):
    print("This goes to the string buffer")
    print("Not to the console")

print(f"Captured output: {output.getvalue()}")

# contextlib.redirect_stderr
from contextlib import redirect_stderr

# Redirect stderr
error_output = io.StringIO()
with redirect_stderr(error_output):
    print("This is an error message", file=sys.stderr)

print(f"Captured error: {error_output.getvalue()}")

# 7. Exception Handling in Context Managers
print("\n=== Exception Handling in Context Managers ===")

class ExceptionHandlingManager:
    """Context manager with exception handling"""
    
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        
        if exc_type is None:
            print("No exception occurred")
        else:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
            
            # Handle specific exceptions
            if exc_type == ValueError:
                print("Handling ValueError")
                return True  # Suppress the exception
            
            if exc_type == TypeError:
                print("Handling TypeError")
                return False  # Let the exception propagate
        
        return False

# Test exception handling
with ExceptionHandlingManager():
    print("Normal operation")

try:
    with ExceptionHandlingManager():
        raise ValueError("Test error")
except ValueError:
    print("ValueError was suppressed")

try:
    with ExceptionHandlingManager():
        raise TypeError("Test error")
except TypeError:
    print("TypeError was not suppressed")

# 8. Practical Context Manager Examples
print("\n=== Practical Context Manager Examples ===")

# Example 1: Timer Context Manager
import time

class Timer:
    """Context manager for timing code execution"""
    
    def __init__(self, name="Operation"):
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        print(f"Starting {self.name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        print(f"{self.name} completed in {duration:.4f} seconds")
        return False

# Use timer context manager
with Timer("Data Processing"):
    time.sleep(0.1)  # Simulate work
    print("Processing data...")

# Example 2: Database Transaction Manager
class TransactionManager:
    """Context manager for database transactions"""
    
    def __init__(self, connection):
        self.connection = connection
        self.transaction_started = False
    
    def __enter__(self):
        print("Starting transaction")
        self.transaction_started = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Committing transaction")
            # Commit transaction
        else:
            print("Rolling back transaction")
            # Rollback transaction
        
        self.transaction_started = False
        return False
    
    def execute_query(self, query):
        """Execute a query within the transaction"""
        if not self.transaction_started:
            raise RuntimeError("Not in a transaction")
        print(f"Executing: {query}")

# Use transaction manager
with TransactionManager("mock_connection") as tx:
    tx.execute_query("INSERT INTO users VALUES (1, 'Alice')")
    tx.execute_query("UPDATE users SET name = 'Bob' WHERE id = 1")

# Example 3: Resource Pool Manager
class ResourcePool:
    """Context manager for resource pooling"""
    
    def __init__(self, pool_size=5):
        self.pool_size = pool_size
        self.available_resources = list(range(pool_size))
        self.used_resources = set()
    
    def __enter__(self):
        if not self.available_resources:
            raise RuntimeError("No resources available")
        
        resource = self.available_resources.pop()
        self.used_resources.add(resource)
        print(f"Acquired resource: {resource}")
        return resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Return resource to pool
        if hasattr(self, '_current_resource'):
            resource = self._current_resource
            self.used_resources.discard(resource)
            self.available_resources.append(resource)
            print(f"Released resource: {resource}")
        return False

# Use resource pool
pool = ResourcePool(3)

with pool as resource1:
    print(f"Using resource {resource1}")
    
    with pool as resource2:
        print(f"Using resource {resource2}")

# 9. Advanced Context Manager Patterns
print("\n=== Advanced Context Manager Patterns ===")

# Pattern 1: Context Manager with State
class StatefulContextManager:
    """Context manager that maintains state"""
    
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.current_state = None
    
    def __enter__(self):
        self.current_state = self.initial_state
        print(f"Initialized with state: {self.current_state}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Final state: {self.current_state}")
        return False
    
    def update_state(self, new_state):
        """Update the current state"""
        self.current_state = new_state
        print(f"State updated to: {self.current_state}")

# Use stateful context manager
with StatefulContextManager("initial") as cm:
    cm.update_state("processing")
    cm.update_state("completed")

# Pattern 2: Nested Context Managers
class NestedContextManager:
    """Context manager that can be nested"""
    
    def __init__(self, name):
        self.name = name
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        print(f"{'  ' * (self.level - 1)}Entering {self.name} (level {self.level})")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{'  ' * (self.level - 1)}Exiting {self.name} (level {self.level})")
        self.level -= 1
        return False

# Use nested context managers
with NestedContextManager("outer") as outer:
    with NestedContextManager("inner") as inner:
        print("  Nested operation")

# Pattern 3: Context Manager with Cleanup
class CleanupContextManager:
    """Context manager with cleanup operations"""
    
    def __init__(self):
        self.cleanup_operations = []
    
    def __enter__(self):
        print("Setting up context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning up context")
        for operation in reversed(self.cleanup_operations):
            try:
                operation()
            except Exception as e:
                print(f"Cleanup error: {e}")
        return False
    
    def add_cleanup(self, operation):
        """Add a cleanup operation"""
        self.cleanup_operations.append(operation)

# Use cleanup context manager
with CleanupContextManager() as cm:
    cm.add_cleanup(lambda: print("Cleanup 1"))
    cm.add_cleanup(lambda: print("Cleanup 2"))
    print("Main operation")

# 10. Context Manager Best Practices
print("\n=== Context Manager Best Practices ===")

# Best Practice 1: Always handle exceptions properly
class ProperExceptionHandling:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # Log the exception
            print(f"Exception in context: {exc_type.__name__}: {exc_val}")
            # Don't suppress exceptions unless necessary
            return False
        return False

# Best Practice 2: Use contextlib utilities when appropriate
from contextlib import contextmanager

@contextmanager
def simple_context():
    print("Setup")
    try:
        yield
    finally:
        print("Cleanup")

# Best Practice 3: Document context manager behavior
class DocumentedContextManager:
    """
    Context manager that demonstrates proper documentation.
    
    This context manager handles resource acquisition and release.
    It ensures proper cleanup even if exceptions occur.
    """
    
    def __enter__(self):
        """Enter the context and acquire resources."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context and release resources."""
        return False

# Best Practice 4: Use context managers for resource management
class ResourceManager:
    """Manage resources with proper cleanup"""
    
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.resource = None
    
    def __enter__(self):
        print(f"Acquiring {self.resource_name}")
        self.resource = f"Resource: {self.resource_name}"
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing {self.resource_name}")
        self.resource = None
        return False

# 11. Real-world Context Manager Examples
print("\n=== Real-world Context Manager Examples ===")

# Example 1: API Rate Limiting
class RateLimiter:
    """Context manager for API rate limiting"""
    
    def __init__(self, max_requests=10, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
    
    def __enter__(self):
        current_time = time.time()
        # Remove old requests
        self.requests = [req_time for req_time in self.requests 
                        if current_time - req_time < self.time_window]
        
        if len(self.requests) >= self.max_requests:
            raise RuntimeError("Rate limit exceeded")
        
        self.requests.append(current_time)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

# Use rate limiter
try:
    with RateLimiter(max_requests=2, time_window=1):
        print("API request made")
except RuntimeError as e:
    print(f"Rate limit error: {e}")

# Example 2: Configuration Management
class ConfigManager:
    """Context manager for configuration management"""
    
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.original_config = {}
    
    def __enter__(self):
        # Save original configuration
        import os
        for key, value in self.config_dict.items():
            self.original_config[key] = os.environ.get(key)
            os.environ[key] = str(value)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore original configuration
        import os
        for key, original_value in self.original_config.items():
            if original_value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = original_value
        return False

# Use configuration manager
with ConfigManager({"DEBUG": "True", "LOG_LEVEL": "DEBUG"}):
    print("Configuration applied")

# Example 3: Database Connection Pool
class ConnectionPool:
    """Context manager for database connection pooling"""
    
    def __init__(self, pool_size=5):
        self.pool_size = pool_size
        self.connections = list(range(pool_size))
        self.used_connections = set()
    
    def __enter__(self):
        if not self.connections:
            raise RuntimeError("No connections available")
        
        connection = self.connections.pop()
        self.used_connections.add(connection)
        print(f"Acquired connection: {connection}")
        return connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Return connection to pool
        if hasattr(self, '_current_connection'):
            connection = self._current_connection
            self.used_connections.discard(connection)
            self.connections.append(connection)
            print(f"Released connection: {connection}")
        return False

# Use connection pool
pool = ConnectionPool(3)

with pool as conn1:
    print(f"Using connection {conn1}")
    
    with pool as conn2:
        print(f"Using connection {conn2}")

# 12. Context Manager Testing
print("\n=== Context Manager Testing ===")

# Test context manager behavior
class TestableContextManager:
    """Context manager designed for testing"""
    
    def __init__(self):
        self.entered = False
        self.exited = False
        self.exception_handled = False
    
    def __enter__(self):
        self.entered = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exited = True
        if exc_type:
            self.exception_handled = True
        return False

# Test normal operation
cm = TestableContextManager()
with cm:
    pass

print(f"Entered: {cm.entered}")
print(f"Exited: {cm.exited}")
print(f"Exception handled: {cm.exception_handled}")

# Test with exception
cm = TestableContextManager()
try:
    with cm:
        raise ValueError("Test error")
except ValueError:
    pass

print(f"Entered: {cm.entered}")
print(f"Exited: {cm.exited}")
print(f"Exception handled: {cm.exception_handled}")

# Cleanup
import os
files_to_remove = ["sample.txt", "custom.txt", "decorator.txt", "file1.txt", "file2.txt"]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)

# Exercises:
"""
1. Create a context manager that measures execution time
2. Write a context manager that temporarily changes the working directory
3. Create a context manager that handles database transactions
4. Write a context manager that manages file locks
5. Create a context manager that handles API rate limiting
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Execution time context manager
print("Exercise 1: Execution Time Context Manager")
class ExecutionTimer:
    def __init__(self, name="Operation"):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"{self.name} took {duration:.4f} seconds")
        return False

with ExecutionTimer("Test Operation"):
    time.sleep(0.1)

# 2. Working directory context manager
print("\nExercise 2: Working Directory Context Manager")
class WorkingDirectory:
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.original_dir = None
    
    def __enter__(self):
        self.original_dir = os.getcwd()
        os.chdir(self.new_dir)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
        return False

# Test working directory change
original_dir = os.getcwd()
with WorkingDirectory("/tmp"):
    print(f"Current directory: {os.getcwd()}")
print(f"Back to original: {os.getcwd()}")

# 3. Database transaction context manager
print("\nExercise 3: Database Transaction Context Manager")
class DatabaseTransaction:
    def __init__(self, connection):
        self.connection = connection
        self.transaction_started = False
    
    def __enter__(self):
        print("Starting transaction")
        self.transaction_started = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Committing transaction")
        else:
            print("Rolling back transaction")
        self.transaction_started = False
        return False

with DatabaseTransaction("mock_connection"):
    print("Executing queries...")

# 4. File lock context manager
print("\nExercise 4: File Lock Context Manager")
class FileLock:
    def __init__(self, filename):
        self.filename = filename
        self.lock_file = f"{filename}.lock"
        self.locked = False
    
    def __enter__(self):
        if os.path.exists(self.lock_file):
            raise RuntimeError(f"File {self.filename} is locked")
        
        with open(self.lock_file, "w") as f:
            f.write(str(os.getpid()))
        self.locked = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.locked:
            os.remove(self.lock_file)
        return False

# Test file lock
with FileLock("test_file.txt"):
    print("File is locked")

# 5. API rate limiting context manager
print("\nExercise 5: API Rate Limiting Context Manager")
class APIRateLimit:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
    
    def __enter__(self):
        current_time = time.time()
        self.requests = [req_time for req_time in self.requests 
                        if current_time - req_time < self.time_window]
        
        if len(self.requests) >= self.max_requests:
            raise RuntimeError("API rate limit exceeded")
        
        self.requests.append(current_time)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

# Test API rate limiting
try:
    with APIRateLimit(max_requests=2, time_window=1):
        print("API request made")
except RuntimeError as e:
    print(f"Rate limit error: {e}")

print("\n🎉 Congratulations! You've completed Lesson 23!")
print("Next: Lesson 24 - Iterators")
