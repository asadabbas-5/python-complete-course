# Lesson 14: Exception Handling

"""
This lesson covers:
- What are exceptions and errors
- try, except, else, finally blocks
- Different types of exceptions
- Raising custom exceptions
- Exception handling best practices
- Context managers and exceptions
- Logging exceptions
"""

# 1. Basic Exception Handling
print("=== Basic Exception Handling ===")

# Division by zero error
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# File not found error
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")

# Multiple exception types
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("Error: Invalid number format!")
except ZeroDivisionError:
    print("Error: Division by zero!")

# 2. try, except, else, finally
print("\n=== try, except, else, finally ===")

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid data types!")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("This always executes!")

# Test the function
print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"'10' / 2 = {divide_numbers('10', 2)}")

# 3. Catching All Exceptions
print("\n=== Catching All Exceptions ===")

def safe_operation():
    try:
        # This will cause a NameError
        undefined_variable = some_undefined_variable
    except Exception as e:
        print(f"Caught exception: {type(e).__name__}: {e}")

safe_operation()

# More specific exception handling
def better_safe_operation():
    try:
        undefined_variable = some_undefined_variable
    except NameError as e:
        print(f"NameError: {e}")
    except Exception as e:
        print(f"Other exception: {type(e).__name__}: {e}")

better_safe_operation()

# 4. Common Built-in Exceptions
print("\n=== Common Built-in Exceptions ===")

# ValueError
try:
    int("not_a_number")
except ValueError as e:
    print(f"ValueError: {e}")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"KeyError: {e}")

# TypeError
try:
    "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# AttributeError
try:
    my_string = "hello"
    my_string.append("world")
except AttributeError as e:
    print(f"AttributeError: {e}")

# 5. Raising Exceptions
print("\n=== Raising Exceptions ===")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot be greater than 150")
    return True

# Test validation
test_ages = [25, -5, "twenty", 200]
for age in test_ages:
    try:
        validate_age(age)
        print(f"Age {age} is valid")
    except (TypeError, ValueError) as e:
        print(f"Age {age} is invalid: {e}")

# 6. Custom Exceptions
print("\n=== Custom Exceptions ===")

class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class ValidationError(CustomError):
    """Raised when validation fails"""
    def __init__(self, message, field=None):
        self.field = field
        super().__init__(message)

class DatabaseError(CustomError):
    """Raised when database operation fails"""
    def __init__(self, message, error_code=None):
        self.error_code = error_code
        super().__init__(message)

def validate_user_data(name, email):
    if not name or not name.strip():
        raise ValidationError("Name cannot be empty", field="name")
    
    if not email or "@" not in email:
        raise ValidationError("Invalid email format", field="email")
    
    return True

# Test custom exceptions
test_data = [
    ("Alice", "alice@example.com"),
    ("", "bob@example.com"),
    ("Charlie", "invalid-email")
]

for name, email in test_data:
    try:
        validate_user_data(name, email)
        print(f"User data valid: {name}, {email}")
    except ValidationError as e:
        print(f"Validation error: {e} (Field: {e.field})")

# 7. Exception Chaining
print("\n=== Exception Chaining ===")

def process_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            # Simulate processing error
            if "error" in content.lower():
                raise ValueError("Content contains error")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not process file '{filename}'") from e

try:
    process_file("nonexistent.txt")
except FileNotFoundError as e:
    print(f"File error: {e}")
    print(f"Caused by: {e.__cause__}")

# 8. Exception Handling in Classes
print("\n=== Exception Handling in Classes ===")

class Calculator:
    def __init__(self):
        self.history = []
    
    def divide(self, a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Both arguments must be numbers")
            
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            
            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            return result
            
        except (TypeError, ZeroDivisionError) as e:
            self.history.append(f"Error: {e}")
            raise
    
    def get_history(self):
        return self.history.copy()

# Test calculator
calc = Calculator()
try:
    result = calc.divide(10, 2)
    print(f"10 / 2 = {result}")
except Exception as e:
    print(f"Error: {e}")

try:
    result = calc.divide(10, 0)
except Exception as e:
    print(f"Error: {e}")

print(f"Calculator history: {calc.get_history()}")

# 9. Context Managers and Exceptions
print("\n=== Context Managers and Exceptions ===")

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to database: {self.connection_string}")
        # Simulate connection
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        self.connected = False
        
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
            # Return False to let the exception propagate
            return False
        
        return True
    
    def execute_query(self, query):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        
        if "error" in query.lower():
            raise ValueError("Query contains error")
        
        print(f"Executing query: {query}")
        return f"Result for: {query}"

# Test context manager
try:
    with DatabaseConnection("localhost:5432") as db:
        result = db.execute_query("SELECT * FROM users")
        print(f"Query result: {result}")
except Exception as e:
    print(f"Database error: {e}")

# 10. Exception Handling Best Practices
print("\n=== Exception Handling Best Practices ===")

# Best Practice 1: Be specific with exceptions
def good_exception_handling():
    try:
        # Some operation that might fail
        data = {"key": "value"}
        value = data["nonexistent_key"]
    except KeyError as e:
        print(f"Key not found: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Best Practice 2: Don't catch exceptions you can't handle
def process_data(data):
    """Process data and let exceptions propagate if needed"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    # Process data...
    return data.upper()

# Best Practice 3: Use finally for cleanup
def safe_file_operation(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    finally:
        if file:
            file.close()
            print("File closed")

# Best Practice 4: Log exceptions
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def logged_operation():
    try:
        # Some operation that might fail
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.error(f"Division by zero: {e}")
        raise

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Robust File Processor
class FileProcessor:
    def __init__(self):
        self.processed_files = 0
        self.errors = []
    
    def process_file(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
            
            # Process content
            processed_content = content.upper()
            
            # Write processed content
            output_filename = f"processed_{filename}"
            with open(output_filename, "w") as file:
                file.write(processed_content)
            
            self.processed_files += 1
            print(f"Successfully processed: {filename}")
            
        except FileNotFoundError:
            error_msg = f"File not found: {filename}"
            self.errors.append(error_msg)
            print(error_msg)
        except PermissionError:
            error_msg = f"Permission denied: {filename}"
            self.errors.append(error_msg)
            print(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error processing {filename}: {e}"
            self.errors.append(error_msg)
            print(error_msg)
    
    def get_stats(self):
        return {
            "processed_files": self.processed_files,
            "errors": len(self.errors),
            "error_details": self.errors
        }

# Test file processor
processor = FileProcessor()
processor.process_file("nonexistent.txt")
processor.process_file("sample.txt")  # This will also fail

stats = processor.get_stats()
print(f"Processing stats: {stats}")

# Example 2: API Client with Error Handling
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session_count = 0
    
    def make_request(self, endpoint, data=None):
        try:
            self.session_count += 1
            
            # Simulate API call
            if endpoint == "error":
                raise ConnectionError("API server unavailable")
            
            if data and "invalid" in str(data):
                raise ValueError("Invalid data format")
            
            return {"status": "success", "data": data}
            
        except ConnectionError as e:
            print(f"Connection error: {e}")
            return {"status": "error", "message": str(e)}
        except ValueError as e:
            print(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {"status": "error", "message": "Internal error"}

# Test API client
client = APIClient("https://api.example.com")

# Successful request
response = client.make_request("users", {"name": "Alice"})
print(f"API Response: {response}")

# Error request
response = client.make_request("error")
print(f"API Response: {response}")

# Validation error
response = client.make_request("users", {"data": "invalid"})
print(f"API Response: {response}")

# Example 3: Retry Mechanism with Exceptions
def retry_operation(operation, max_retries=3, delay=1):
    """Retry an operation with exponential backoff"""
    import time
    
    for attempt in range(max_retries):
        try:
            return operation()
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"Operation failed after {max_retries} attempts: {e}")
                raise
            
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay * (2 ** attempt))  # Exponential backoff

def unreliable_operation():
    """An operation that might fail"""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network timeout")
    return "Operation successful"

# Test retry mechanism
try:
    result = retry_operation(unreliable_operation, max_retries=3)
    print(f"Final result: {result}")
except Exception as e:
    print(f"All retries failed: {e}")

# 12. Exception Handling Patterns
print("\n=== Exception Handling Patterns ===")

# Pattern 1: Exception Translation
class DataProcessor:
    def process(self, data):
        try:
            # Some processing that might raise various exceptions
            if not data:
                raise ValueError("Empty data")
            
            result = data.upper()
            return result
            
        except ValueError as e:
            # Translate to domain-specific exception
            raise ProcessingError(f"Data processing failed: {e}") from e
        except Exception as e:
            # Translate to generic processing error
            raise ProcessingError(f"Unexpected processing error: {e}") from e

class ProcessingError(Exception):
    """Domain-specific exception for processing errors"""
    pass

# Pattern 2: Exception Suppression
def safe_divide(a, b):
    """Divide two numbers, return None if division fails"""
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None

# Pattern 3: Exception Aggregation
class BatchProcessor:
    def __init__(self):
        self.errors = []
    
    def process_items(self, items):
        results = []
        
        for item in items:
            try:
                result = self.process_item(item)
                results.append(result)
            except Exception as e:
                self.errors.append(f"Failed to process {item}: {e}")
        
        if self.errors:
            raise BatchProcessingError(f"Batch processing failed: {self.errors}")
        
        return results
    
    def process_item(self, item):
        # Simulate item processing
        if item == "error":
            raise ValueError("Item processing failed")
        return f"Processed: {item}"

class BatchProcessingError(Exception):
    """Exception for batch processing failures"""
    pass

# Test batch processor
processor = BatchProcessor()
try:
    results = processor.process_items(["item1", "error", "item3"])
    print(f"Results: {results}")
except BatchProcessingError as e:
    print(f"Batch error: {e}")

# Exercises:
"""
1. Write a function that safely converts a string to an integer
2. Create a class that handles file operations with proper exception handling
3. Write a function that retries a failed operation with exponential backoff
4. Create a custom exception hierarchy for a banking application
5. Write a function that validates user input with detailed error messages
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Safe string to integer conversion
print("Exercise 1: Safe String to Integer")
def safe_int_conversion(value, default=None):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer")
        return default
    except TypeError:
        print(f"Invalid type for conversion: {type(value)}")
        return default

test_values = ["123", "abc", "45.6", None, 789]
for value in test_values:
    result = safe_int_conversion(value, default=0)
    print(f"safe_int_conversion('{value}') = {result}")

# 2. File operations class
print("\nExercise 2: File Operations Class")
class SafeFileHandler:
    def __init__(self):
        self.open_files = []
    
    def read_file(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found")
        except PermissionError:
            raise PermissionError(f"Permission denied for '{filename}'")
        except Exception as e:
            raise Exception(f"Error reading '{filename}': {e}")
    
    def write_file(self, filename, content):
        try:
            with open(filename, "w") as file:
                file.write(content)
            print(f"Successfully wrote to '{filename}'")
        except PermissionError:
            raise PermissionError(f"Permission denied for '{filename}'")
        except Exception as e:
            raise Exception(f"Error writing to '{filename}': {e}")

# Test file handler
file_handler = SafeFileHandler()
try:
    file_handler.write_file("test.txt", "Hello, World!")
    content = file_handler.read_file("test.txt")
    print(f"Read content: {content}")
except Exception as e:
    print(f"File operation error: {e}")

# 3. Retry with exponential backoff
print("\nExercise 3: Retry with Exponential Backoff")
def retry_with_backoff(func, max_retries=3, base_delay=1):
    import time
    import random
    
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.2f}s...")
            time.sleep(delay)

def unreliable_function():
    import random
    if random.random() < 0.8:
        raise ConnectionError("Connection failed")
    return "Success!"

try:
    result = retry_with_backoff(unreliable_function, max_retries=3)
    print(f"Final result: {result}")
except Exception as e:
    print(f"All retries failed: {e}")

# 4. Banking exception hierarchy
print("\nExercise 4: Banking Exception Hierarchy")
class BankingError(Exception):
    """Base exception for banking operations"""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds"""
    pass

class InvalidAccountError(BankingError):
    """Raised when account is invalid"""
    pass

class TransactionError(BankingError):
    """Raised when transaction fails"""
    pass

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise TransactionError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Balance: {self.balance}")
        
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise TransactionError("Deposit amount must be positive")
        
        self.balance += amount
        return self.balance

# Test banking operations
account = BankAccount("12345", 100)
try:
    account.withdraw(50)
    print(f"Withdrawal successful. Balance: {account.balance}")
    account.withdraw(100)  # This will fail
except InsufficientFundsError as e:
    print(f"Banking error: {e}")
except TransactionError as e:
    print(f"Transaction error: {e}")

# 5. Input validation with detailed errors
print("\nExercise 5: Input Validation")
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

def validate_user_input(data):
    errors = []
    
    # Validate name
    if "name" not in data:
        errors.append(ValidationError("name", "Name is required"))
    elif not isinstance(data["name"], str):
        errors.append(ValidationError("name", "Name must be a string"))
    elif len(data["name"].strip()) < 2:
        errors.append(ValidationError("name", "Name must be at least 2 characters"))
    
    # Validate age
    if "age" not in data:
        errors.append(ValidationError("age", "Age is required"))
    elif not isinstance(data["age"], int):
        errors.append(ValidationError("age", "Age must be an integer"))
    elif data["age"] < 0 or data["age"] > 150:
        errors.append(ValidationError("age", "Age must be between 0 and 150"))
    
    # Validate email
    if "email" not in data:
        errors.append(ValidationError("email", "Email is required"))
    elif not isinstance(data["email"], str):
        errors.append(ValidationError("email", "Email must be a string"))
    elif "@" not in data["email"]:
        errors.append(ValidationError("email", "Email must contain @ symbol"))
    
    if errors:
        raise ValidationError("validation", f"Multiple validation errors: {[str(e) for e in errors]}")

# Test validation
test_data = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "", "age": -5, "email": "invalid-email"},
    {"age": 30, "email": "bob@example.com"}
]

for data in test_data:
    try:
        validate_user_input(data)
        print(f"Validation passed for: {data}")
    except ValidationError as e:
        print(f"Validation failed: {e}")

# Cleanup
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")

print("\n🎉 Congratulations! You've completed Lesson 14!")
print("Next: Lesson 15 - Modules and Packages")
