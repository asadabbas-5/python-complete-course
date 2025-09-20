# Lesson 15: Modules and Packages

"""
This lesson covers:
- What are modules and packages
- Creating and importing modules
- Package structure and organization
- Import statements and variations
- Module search path and sys.path
- __init__.py files
- Relative vs absolute imports
- Module reloading and caching
"""

# 1. What are Modules and Packages
print("=== What are Modules and Packages ===")

# A module is a Python file containing definitions and statements
# A package is a directory containing multiple modules and an __init__.py file

# Built-in modules
import math
import random
import datetime

print(f"Math module: {math}")
print(f"Random module: {random}")
print(f"Datetime module: {datetime}")

# Using module functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number: {random.randint(1, 10)}")
print(f"Current time: {datetime.datetime.now()}")

# 2. Creating a Simple Module
print("\n=== Creating a Simple Module ===")

# Let's create a simple module file
module_content = '''
# math_utils.py - A simple math utilities module

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def power(base, exponent):
    """Calculate base raised to the power of exponent"""
    return base ** exponent

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Module-level variables
PI = 3.14159
E = 2.71828

# Module-level code (executed when imported)
print("Math utils module loaded!")
'''

# Write the module to a file
with open("math_utils.py", "w") as f:
    f.write(module_content)

# Import our custom module
import math_utils

print(f"Math utils module: {math_utils}")
print(f"PI constant: {math_utils.PI}")
print(f"Add 5 + 3: {math_utils.add(5, 3)}")
print(f"Multiply 4 * 6: {math_utils.multiply(4, 6)}")
print(f"Power 2^8: {math_utils.power(2, 8)}")
print(f"Factorial of 5: {math_utils.factorial(5)}")

# 3. Different Import Methods
print("\n=== Different Import Methods ===")

# Method 1: Import entire module
import math_utils
result1 = math_utils.add(10, 20)

# Method 2: Import specific functions
from math_utils import add, multiply
result2 = add(10, 20)
result3 = multiply(5, 6)

# Method 3: Import with alias
from math_utils import power as pow_func
result4 = pow_func(2, 3)

# Method 4: Import all (not recommended)
from math_utils import *
result5 = factorial(4)

print(f"Results: {result1}, {result2}, {result3}, {result4}, {result5}")

# 4. Creating a Package
print("\n=== Creating a Package ===")

import os

# Create package directory structure
os.makedirs("my_package", exist_ok=True)
os.makedirs("my_package/subpackage", exist_ok=True)

# Create __init__.py files
with open("my_package/__init__.py", "w") as f:
    f.write('''
# my_package/__init__.py

# Package-level imports
from .core import CoreClass
from .utils import utility_function

# Package-level variables
VERSION = "1.0.0"
AUTHOR = "Python Course"

# Package-level code
print("My package loaded!")

# Make specific items available when importing the package
__all__ = ['CoreClass', 'utility_function', 'VERSION', 'AUTHOR']
''')

# Create core module
with open("my_package/core.py", "w") as f:
    f.write('''
# my_package/core.py

class CoreClass:
    """Core functionality class"""
    
    def __init__(self, name):
        self.name = name
        self.data = []
    
    def add_data(self, item):
        """Add item to data"""
        self.data.append(item)
        return len(self.data)
    
    def get_data(self):
        """Get all data"""
        return self.data.copy()
    
    def process_data(self):
        """Process the data"""
        return [item.upper() if isinstance(item, str) else item for item in self.data]

def core_function():
    """Core utility function"""
    return "Core function executed"
''')

# Create utils module
with open("my_package/utils.py", "w") as f:
    f.write('''
# my_package/utils.py

def utility_function():
    """A utility function"""
    return "Utility function executed"

def helper_function():
    """A helper function"""
    return "Helper function executed"

def format_data(data):
    """Format data for display"""
    if isinstance(data, list):
        return ", ".join(str(item) for item in data)
    return str(data)
''')

# Create subpackage
with open("my_package/subpackage/__init__.py", "w") as f:
    f.write('''
# my_package/subpackage/__init__.py

from .advanced import AdvancedClass

__all__ = ['AdvancedClass']
''')

with open("my_package/subpackage/advanced.py", "w") as f:
    f.write('''
# my_package/subpackage/advanced.py

class AdvancedClass:
    """Advanced functionality class"""
    
    def __init__(self):
        self.features = []
    
    def add_feature(self, feature):
        """Add a feature"""
        self.features.append(feature)
    
    def get_features(self):
        """Get all features"""
        return self.features.copy()
''')

# 5. Importing from Packages
print("\n=== Importing from Packages ===")

# Import the package
import my_package

print(f"Package version: {my_package.VERSION}")
print(f"Package author: {my_package.AUTHOR}")

# Use imported classes and functions
core = my_package.CoreClass("Test")
core.add_data("hello")
core.add_data("world")
print(f"Core data: {core.get_data()}")
print(f"Processed data: {core.process_data()}")

utility_result = my_package.utility_function()
print(f"Utility result: {utility_result}")

# Import from subpackage
from my_package.subpackage import AdvancedClass
advanced = AdvancedClass()
advanced.add_feature("feature1")
advanced.add_feature("feature2")
print(f"Advanced features: {advanced.get_features()}")

# 6. Relative vs Absolute Imports
print("\n=== Relative vs Absolute Imports ===")

# Absolute imports (recommended)
from my_package.core import CoreClass
from my_package.utils import utility_function

# Relative imports (used within packages)
# from .core import CoreClass  # Same level
# from ..parent import ParentClass  # Parent level
# from .subpackage.advanced import AdvancedClass  # Subpackage

# Example of relative import in a module
relative_import_content = '''
# Example of relative imports within a package
from .core import CoreClass
from .utils import utility_function
from .subpackage.advanced import AdvancedClass
'''

# 7. Module Search Path
print("\n=== Module Search Path ===")

import sys

print("Python module search path:")
for i, path in enumerate(sys.path):
    print(f"{i}: {path}")

# Adding custom path
custom_path = os.path.abspath(".")
if custom_path not in sys.path:
    sys.path.append(custom_path)
    print(f"Added custom path: {custom_path}")

# 8. Module Reloading
print("\n=== Module Reloading ===")

import importlib

# Reload a module (useful during development)
print("Before reload:")
print(f"Math utils PI: {math_utils.PI}")

# Modify the module file
with open("math_utils.py", "a") as f:
    f.write("\n# Updated PI value\nPI = 3.14159265359\n")

# Reload the module
importlib.reload(math_utils)

print("After reload:")
print(f"Math utils PI: {math_utils.PI}")

# 9. Module Attributes and Inspection
print("\n=== Module Attributes and Inspection ===")

# Inspect module attributes
print(f"Math utils module name: {math_utils.__name__}")
print(f"Math utils file: {math_utils.__file__}")
print(f"Math utils doc: {math_utils.__doc__}")

# Get all attributes of a module
print("Math utils attributes:")
for attr in dir(math_utils):
    if not attr.startswith('_'):  # Skip private attributes
        print(f"  {attr}")

# Check if module has specific attribute
if hasattr(math_utils, 'PI'):
    print(f"PI value: {getattr(math_utils, 'PI')}")

# 10. Package Initialization
print("\n=== Package Initialization ===")

# The __init__.py file controls what happens when a package is imported
# It can:
# - Import submodules
# - Define package-level variables
# - Execute initialization code
# - Control what gets imported with "from package import *"

# Example of a more complex __init__.py
complex_init_content = '''
# Complex package initialization

import os
import sys

# Package configuration
PACKAGE_ROOT = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(PACKAGE_ROOT, 'config.json')

# Import submodules
from .core import CoreClass
from .utils import utility_function, helper_function
from .subpackage.advanced import AdvancedClass

# Package-level functions
def initialize_package():
    """Initialize the package"""
    print("Package initialized!")
    return True

def get_package_info():
    """Get package information"""
    return {
        'name': 'my_package',
        'version': '1.0.0',
        'root': PACKAGE_ROOT
    }

# Execute initialization
initialize_package()

# Control what gets imported with "from package import *"
__all__ = [
    'CoreClass',
    'utility_function',
    'helper_function', 
    'AdvancedClass',
    'initialize_package',
    'get_package_info'
]
'''

# 11. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Configuration Module
config_content = '''
# config.py - Configuration module

import os

class Config:
    """Application configuration"""
    
    def __init__(self):
        self.debug = os.getenv('DEBUG', 'False').lower() == 'true'
        self.port = int(os.getenv('PORT', '8080'))
        self.host = os.getenv('HOST', 'localhost')
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    
    def get_database_config(self):
        """Get database configuration"""
        return {
            'url': self.database_url,
            'echo': self.debug
        }
    
    def get_server_config(self):
        """Get server configuration"""
        return {
            'host': self.host,
            'port': self.port,
            'debug': self.debug
        }

# Global configuration instance
config = Config()
'''

with open("config.py", "w") as f:
    f.write(config_content)

# Import and use config
import config
print(f"Debug mode: {config.config.debug}")
print(f"Server config: {config.config.get_server_config()}")

# Example 2: Utility Package
os.makedirs("utils", exist_ok=True)

# Create utils package
with open("utils/__init__.py", "w") as f:
    f.write('''
# utils/__init__.py

from .file_utils import read_file, write_file
from .string_utils import clean_string, format_string
from .date_utils import format_date, parse_date

__all__ = [
    'read_file', 'write_file',
    'clean_string', 'format_string', 
    'format_date', 'parse_date'
]
''')

with open("utils/file_utils.py", "w") as f:
    f.write('''
# utils/file_utils.py

def read_file(filename):
    """Read file content"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def write_file(filename, content):
    """Write content to file"""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return True
    except Exception:
        return False
''')

with open("utils/string_utils.py", "w") as f:
    f.write('''
# utils/string_utils.py

def clean_string(text):
    """Clean string by removing extra whitespace"""
    return ' '.join(text.split())

def format_string(template, **kwargs):
    """Format string with keyword arguments"""
    return template.format(**kwargs)
''')

with open("utils/date_utils.py", "w") as f:
    f.write('''
# utils/date_utils.py

from datetime import datetime

def format_date(date, format_str="%Y-%m-%d"):
    """Format date to string"""
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    return date.strftime(format_str)

def parse_date(date_str, format_str="%Y-%m-%d"):
    """Parse date string to datetime object"""
    return datetime.strptime(date_str, format_str)
''')

# Use the utils package
from utils import read_file, write_file, clean_string, format_date

# Test file utils
write_file("test_utils.txt", "Hello from utils package!")
content = read_file("test_utils.txt")
print(f"File content: {content}")

# Test string utils
cleaned = clean_string("  hello    world  ")
print(f"Cleaned string: '{cleaned}'")

# Test date utils
formatted_date = format_date("2024-01-15", "%B %d, %Y")
print(f"Formatted date: {formatted_date}")

# Example 3: Plugin System
plugin_system_content = '''
# plugin_system.py - Simple plugin system

import os
import importlib
import sys

class PluginManager:
    """Manages plugins for the application"""
    
    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = plugin_dir
        self.plugins = {}
        self.load_plugins()
    
    def load_plugins(self):
        """Load all plugins from the plugin directory"""
        if not os.path.exists(self.plugin_dir):
            return
        
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith('.py') and not filename.startswith('_'):
                plugin_name = filename[:-3]  # Remove .py extension
                try:
                    module_path = f"{self.plugin_dir}.{plugin_name}"
                    plugin_module = importlib.import_module(module_path)
                    
                    if hasattr(plugin_module, 'Plugin'):
                        plugin_class = getattr(plugin_module, 'Plugin')
                        self.plugins[plugin_name] = plugin_class()
                        print(f"Loaded plugin: {plugin_name}")
                
                except Exception as e:
                    print(f"Failed to load plugin {plugin_name}: {e}")
    
    def get_plugin(self, name):
        """Get a specific plugin"""
        return self.plugins.get(name)
    
    def list_plugins(self):
        """List all loaded plugins"""
        return list(self.plugins.keys())
    
    def execute_plugin_method(self, plugin_name, method_name, *args, **kwargs):
        """Execute a method on a specific plugin"""
        plugin = self.get_plugin(plugin_name)
        if plugin and hasattr(plugin, method_name):
            method = getattr(plugin, method_name)
            return method(*args, **kwargs)
        return None
'''

with open("plugin_system.py", "w") as f:
    f.write(plugin_system_content)

# Create plugins directory and sample plugin
os.makedirs("plugins", exist_ok=True)

with open("plugins/sample_plugin.py", "w") as f:
    f.write('''
# plugins/sample_plugin.py

class Plugin:
    """Sample plugin"""
    
    def __init__(self):
        self.name = "Sample Plugin"
        self.version = "1.0.0"
    
    def process_data(self, data):
        """Process data"""
        return f"Processed by {self.name}: {data.upper()}"
    
    def get_info(self):
        """Get plugin information"""
        return {
            'name': self.name,
            'version': self.version
        }
''')

# Test plugin system
import plugin_system
plugin_manager = plugin_system.PluginManager()
print(f"Loaded plugins: {plugin_manager.list_plugins()}")

# Use plugin
result = plugin_manager.execute_plugin_method("sample_plugin", "process_data", "hello world")
print(f"Plugin result: {result}")

plugin_info = plugin_manager.execute_plugin_method("sample_plugin", "get_info")
print(f"Plugin info: {plugin_info}")

# 12. Best Practices
print("\n=== Best Practices ===")

# Best Practice 1: Use descriptive module names
# Good: user_authentication.py, data_processing.py
# Bad: utils.py, helpers.py, misc.py

# Best Practice 2: Keep modules focused
# Each module should have a single responsibility

# Best Practice 3: Use __init__.py to control package imports
# Make the package interface clean and intuitive

# Best Practice 4: Document your modules
module_docstring_example = '''
"""
Module for handling user authentication.

This module provides classes and functions for:
- User registration and login
- Password validation
- Session management

Example:
    from auth import UserManager
    manager = UserManager()
    manager.register_user("alice", "password123")
"""

# Module code here...
'''

# Best Practice 5: Use absolute imports in production code
# from mypackage.subpackage.module import function

# Best Practice 6: Handle import errors gracefully
try:
    import optional_module
    OPTIONAL_AVAILABLE = True
except ImportError:
    OPTIONAL_AVAILABLE = False
    print("Optional module not available")

# Exercises:
"""
1. Create a module for mathematical operations (add, subtract, multiply, divide)
2. Create a package called 'text_processing' with modules for different text operations
3. Write a module that handles configuration settings
4. Create a simple plugin system that can load and execute plugins
5. Write a module that provides logging functionality
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Math operations module
print("Exercise 1: Math Operations Module")
math_ops_content = '''
# math_operations.py

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def sqrt(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5
'''

with open("math_operations.py", "w") as f:
    f.write(math_ops_content)

import math_operations
print(f"5 + 3 = {math_operations.add(5, 3)}")
print(f"10 - 4 = {math_operations.subtract(10, 4)}")
print(f"6 * 7 = {math_operations.multiply(6, 7)}")
print(f"15 / 3 = {math_operations.divide(15, 3)}")

# 2. Text processing package
print("\nExercise 2: Text Processing Package")
os.makedirs("text_processing", exist_ok=True)

with open("text_processing/__init__.py", "w") as f:
    f.write('''
# text_processing/__init__.py

from .cleaner import clean_text, remove_punctuation
from .formatter import format_text, capitalize_words
from .analyzer import count_words, count_characters

__all__ = [
    'clean_text', 'remove_punctuation',
    'format_text', 'capitalize_words',
    'count_words', 'count_characters'
]
''')

with open("text_processing/cleaner.py", "w") as f:
    f.write('''
# text_processing/cleaner.py

import re

def clean_text(text):
    """Clean text by removing extra whitespace"""
    return re.sub(r'\\s+', ' ', text.strip())

def remove_punctuation(text):
    """Remove punctuation from text"""
    return re.sub(r'[^\\w\\s]', '', text)
''')

with open("text_processing/formatter.py", "w") as f:
    f.write('''
# text_processing/formatter.py

def format_text(text, case='title'):
    """Format text with specified case"""
    if case == 'upper':
        return text.upper()
    elif case == 'lower':
        return text.lower()
    elif case == 'title':
        return text.title()
    else:
        return text

def capitalize_words(text):
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in text.split())
''')

with open("text_processing/analyzer.py", "w") as f:
    f.write('''
# text_processing/analyzer.py

def count_words(text):
    """Count number of words in text"""
    return len(text.split())

def count_characters(text):
    """Count number of characters in text"""
    return len(text)
''')

# Test text processing package
from text_processing import clean_text, format_text, count_words

test_text = "  hello    world!  how are you?  "
cleaned = clean_text(test_text)
formatted = format_text(cleaned, 'title')
word_count = count_words(cleaned)

print(f"Original: '{test_text}'")
print(f"Cleaned: '{cleaned}'")
print(f"Formatted: '{formatted}'")
print(f"Word count: {word_count}")

# 3. Configuration module
print("\nExercise 3: Configuration Module")
config_module_content = '''
# app_config.py

import os
import json

class AppConfig:
    """Application configuration manager"""
    
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from file or environment"""
        config = {
            'debug': os.getenv('DEBUG', 'False').lower() == 'true',
            'port': int(os.getenv('PORT', '8080')),
            'host': os.getenv('HOST', 'localhost'),
            'database_url': os.getenv('DATABASE_URL', 'sqlite:///app.db'),
            'secret_key': os.getenv('SECRET_KEY', 'default-secret-key')
        }
        
        # Try to load from file
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    file_config = json.load(f)
                    config.update(file_config)
            except Exception as e:
                print(f"Error loading config file: {e}")
        
        return config
    
    def get(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set configuration value"""
        self.config[key] = value
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

# Global config instance
config = AppConfig()
'''

with open("app_config.py", "w") as f:
    f.write(config_module_content)

import app_config
print(f"Debug mode: {app_config.config.get('debug')}")
print(f"Port: {app_config.config.get('port')}")
print(f"Host: {app_config.config.get('host')}")

# 4. Simple plugin system
print("\nExercise 4: Simple Plugin System")
simple_plugin_content = '''
# simple_plugin_system.py

import os
import importlib

class SimplePluginManager:
    """Simple plugin manager"""
    
    def __init__(self):
        self.plugins = {}
    
    def load_plugin(self, plugin_name, plugin_module):
        """Load a plugin"""
        try:
            if hasattr(plugin_module, 'Plugin'):
                plugin_class = getattr(plugin_module, 'Plugin')
                self.plugins[plugin_name] = plugin_class()
                return True
        except Exception as e:
            print(f"Error loading plugin {plugin_name}: {e}")
        return False
    
    def execute_plugin(self, plugin_name, method_name, *args, **kwargs):
        """Execute a plugin method"""
        plugin = self.plugins.get(plugin_name)
        if plugin and hasattr(plugin, method_name):
            method = getattr(plugin, method_name)
            return method(*args, **kwargs)
        return None
    
    def list_plugins(self):
        """List all loaded plugins"""
        return list(self.plugins.keys())

# Global plugin manager
plugin_manager = SimplePluginManager()
'''

with open("simple_plugin_system.py", "w") as f:
    f.write(simple_plugin_content)

# Create a sample plugin
sample_plugin_content = '''
# sample_plugin.py

class Plugin:
    """Sample plugin for testing"""
    
    def process(self, data):
        """Process data"""
        return f"Processed: {data.upper()}"
    
    def get_name(self):
        """Get plugin name"""
        return "Sample Plugin"
'''

with open("sample_plugin.py", "w") as f:
    f.write(sample_plugin_content)

# Test plugin system
import simple_plugin_system
import sample_plugin

simple_plugin_system.plugin_manager.load_plugin("sample", sample_plugin)
result = simple_plugin_system.plugin_manager.execute_plugin("sample", "process", "hello world")
print(f"Plugin result: {result}")

# 5. Logging module
print("\nExercise 5: Logging Module")
logging_module_content = '''
# app_logger.py

import logging
import os
from datetime import datetime

class AppLogger:
    """Application logger"""
    
    def __init__(self, name="app", log_file="app.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def debug(self, message):
        """Log debug message"""
        self.logger.debug(message)
    
    def info(self, message):
        """Log info message"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log warning message"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error message"""
        self.logger.error(message)
    
    def critical(self, message):
        """Log critical message"""
        self.logger.critical(message)

# Global logger instance
logger = AppLogger()
'''

with open("app_logger.py", "w") as f:
    f.write(logging_module_content)

import app_logger
app_logger.logger.info("Application started")
app_logger.logger.warning("This is a warning message")
app_logger.logger.error("This is an error message")

# Cleanup created files
cleanup_files = [
    "math_utils.py", "config.py", "plugin_system.py", "math_operations.py",
    "app_config.py", "simple_plugin_system.py", "sample_plugin.py", "app_logger.py",
    "test_utils.txt"
]

for file in cleanup_files:
    if os.path.exists(file):
        os.remove(file)

# Cleanup directories
import shutil
for dir_name in ["my_package", "utils", "text_processing", "plugins"]:
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)

print("\n🎉 Congratulations! You've completed Lesson 15!")
print("Next: Lesson 16 - Object-Oriented Programming")
