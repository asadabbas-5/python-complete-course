# Lesson 13: File Handling

"""
This lesson covers:
- Opening and closing files
- Reading from files
- Writing to files
- File modes and permissions
- Working with different file formats
- Error handling with files
- File operations and utilities
"""

# 1. Basic File Operations
print("=== Basic File Operations ===")

# Writing to a file
filename = "sample.txt"
with open(filename, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling is awesome!\n")

print(f"Created file: {filename}")

# Reading from a file
with open(filename, "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# 2. Different File Modes
print("\n=== Different File Modes ===")

# Append mode
with open(filename, "a") as file:
    file.write("This line was appended.\n")

# Read mode
with open(filename, "r") as file:
    lines = file.readlines()
    print("File lines:")
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")

# 3. Reading Files Line by Line
print("\n=== Reading Files Line by Line ===")

# Method 1: Using readlines()
with open(filename, "r") as file:
    lines = file.readlines()
    print("Using readlines():")
    for line in lines:
        print(f"Line: {line.strip()}")

# Method 2: Using readline()
with open(filename, "r") as file:
    print("\nUsing readline():")
    while True:
        line = file.readline()
        if not line:
            break
        print(f"Line: {line.strip()}")

# Method 3: Iterating over file object
with open(filename, "r") as file:
    print("\nIterating over file:")
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

# 4. Writing Different Data Types
print("\n=== Writing Different Data Types ===")

data_file = "data.txt"

# Writing various data types
with open(data_file, "w") as file:
    file.write("String data\n")
    file.write(str(42) + "\n")  # Convert number to string
    file.write(str(3.14) + "\n")
    file.write(str(True) + "\n")
    file.write("List: " + str([1, 2, 3]) + "\n")
    file.write("Dictionary: " + str({"name": "Alice", "age": 25}) + "\n")

# Reading and converting back
with open(data_file, "r") as file:
    lines = file.readlines()
    print("Read data:")
    for line in lines:
        print(f"Raw: {line.strip()}")
        # Try to convert back to appropriate type
        try:
            if line.strip() == "True":
                print(f"Converted: {True}")
            elif line.strip() == "False":
                print(f"Converted: {False}")
            elif line.strip().isdigit():
                print(f"Converted: {int(line.strip())}")
            elif "." in line.strip() and line.strip().replace(".", "").isdigit():
                print(f"Converted: {float(line.strip())}")
            else:
                print(f"Converted: {line.strip()}")
        except:
            print(f"Could not convert: {line.strip()}")

# 5. Working with CSV Files
print("\n=== Working with CSV Files ===")

import csv

# Writing CSV data
csv_filename = "students.csv"
students_data = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 21, "A"],
    ["Diana", 23, "C"]
]

with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print(f"Created CSV file: {csv_filename}")

# Reading CSV data
with open(csv_filename, "r") as file:
    reader = csv.reader(file)
    print("CSV data:")
    for row in reader:
        print(f"Row: {row}")

# Reading CSV as dictionary
with open(csv_filename, "r") as file:
    reader = csv.DictReader(file)
    print("\nCSV as dictionary:")
    for row in reader:
        print(f"Student: {row}")

# 6. Working with JSON Files
print("\n=== Working with JSON Files ===")

import json

# Writing JSON data
json_filename = "data.json"
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"],
    "is_student": True
}

with open(json_filename, "w") as file:
    json.dump(data, file, indent=2)

print(f"Created JSON file: {json_filename}")

# Reading JSON data
with open(json_filename, "r") as file:
    loaded_data = json.load(file)
    print("JSON data:")
    print(json.dumps(loaded_data, indent=2))

# 7. File Error Handling
print("\n=== File Error Handling ===")

def safe_file_read(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

# Test error handling
content = safe_file_read("nonexistent.txt")
if content is not None:
    print(content)

content = safe_file_read(filename)
if content is not None:
    print(f"Successfully read {len(content)} characters")

# 8. File Operations and Utilities
print("\n=== File Operations and Utilities ===")

import os
import shutil

# Check if file exists
print(f"File '{filename}' exists: {os.path.exists(filename)}")

# Get file information
if os.path.exists(filename):
    stat_info = os.stat(filename)
    print(f"File size: {stat_info.st_size} bytes")
    print(f"Last modified: {stat_info.st_mtime}")

# List files in directory
print("Files in current directory:")
for file in os.listdir("."):
    if os.path.isfile(file):
        print(f"  {file}")

# Copy file
if os.path.exists(filename):
    shutil.copy(filename, "copy_of_sample.txt")
    print("File copied successfully")

# Rename file
if os.path.exists("copy_of_sample.txt"):
    os.rename("copy_of_sample.txt", "renamed_sample.txt")
    print("File renamed successfully")

# 9. Working with Binary Files
print("\n=== Working with Binary Files ===")

# Writing binary data
binary_filename = "data.bin"
data = b"Hello, Binary World!\x00\x01\x02\x03"

with open(binary_filename, "wb") as file:
    file.write(data)

print(f"Created binary file: {binary_filename}")

# Reading binary data
with open(binary_filename, "rb") as file:
    binary_content = file.read()
    print(f"Binary content: {binary_content}")
    print(f"Binary content as hex: {binary_content.hex()}")

# 10. File Context Managers
print("\n=== File Context Managers ===")

class FileManager:
    """Custom file manager with context manager support"""
    
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

# Using custom context manager
with FileManager("context_test.txt", "w") as file:
    file.write("This file was created using a custom context manager.\n")

# 11. Working with Large Files
print("\n=== Working with Large Files ===")

def process_large_file(filename, chunk_size=1024):
    """Process a large file in chunks"""
    try:
        with open(filename, "r") as file:
            chunk_count = 0
            total_chars = 0
            
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                
                chunk_count += 1
                total_chars += len(chunk)
                
                # Process chunk (example: count characters)
                char_count = len(chunk)
                print(f"Chunk {chunk_count}: {char_count} characters")
            
            print(f"Total chunks processed: {chunk_count}")
            print(f"Total characters: {total_chars}")
            
    except FileNotFoundError:
        print(f"File '{filename}' not found")

# Test with our sample file
process_large_file(filename, chunk_size=20)

# 12. File Search and Filtering
print("\n=== File Search and Filtering ===")

def search_in_file(filename, search_term):
    """Search for a term in a file"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            matches = []
            
            for line_num, line in enumerate(lines, 1):
                if search_term.lower() in line.lower():
                    matches.append((line_num, line.strip()))
            
            return matches
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return []

# Search in our sample file
search_term = "Python"
matches = search_in_file(filename, search_term)
print(f"Search results for '{search_term}':")
for line_num, line in matches:
    print(f"  Line {line_num}: {line}")

# 13. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Log File Analyzer
class LogAnalyzer:
    def __init__(self, log_filename):
        self.log_filename = log_filename
    
    def count_errors(self):
        """Count error entries in log file"""
        error_count = 0
        try:
            with open(self.log_filename, "r") as file:
                for line in file:
                    if "ERROR" in line.upper():
                        error_count += 1
        except FileNotFoundError:
            print(f"Log file '{self.log_filename}' not found")
        return error_count
    
    def get_recent_entries(self, n=5):
        """Get the last n entries from log file"""
        try:
            with open(self.log_filename, "r") as file:
                lines = file.readlines()
                return lines[-n:] if len(lines) >= n else lines
        except FileNotFoundError:
            return []

# Create a sample log file
log_filename = "app.log"
with open(log_filename, "w") as file:
    file.write("2024-01-01 10:00:00 INFO: Application started\n")
    file.write("2024-01-01 10:01:00 INFO: User logged in\n")
    file.write("2024-01-01 10:02:00 ERROR: Database connection failed\n")
    file.write("2024-01-01 10:03:00 INFO: Retrying connection\n")
    file.write("2024-01-01 10:04:00 ERROR: Still cannot connect\n")
    file.write("2024-01-01 10:05:00 INFO: Using backup database\n")

# Analyze log file
analyzer = LogAnalyzer(log_filename)
error_count = analyzer.count_errors()
recent_entries = analyzer.get_recent_entries(3)

print(f"Error count: {error_count}")
print("Recent entries:")
for entry in recent_entries:
    print(f"  {entry.strip()}")

# Example 2: Configuration File Manager
class ConfigManager:
    def __init__(self, config_filename):
        self.config_filename = config_filename
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from file"""
        try:
            with open(self.config_filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if "=" in line:
                            key, value = line.split("=", 1)
                            self.config[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Config file '{self.config_filename}' not found")
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_filename, "w") as file:
                for key, value in self.config.items():
                    file.write(f"{key}={value}\n")
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set configuration value"""
        self.config[key] = value

# Create sample config file
config_filename = "app.conf"
with open(config_filename, "w") as file:
    file.write("# Application Configuration\n")
    file.write("debug=false\n")
    file.write("port=8080\n")
    file.write("host=localhost\n")
    file.write("max_connections=100\n")

# Use config manager
config = ConfigManager(config_filename)
print(f"Debug mode: {config.get('debug')}")
print(f"Port: {config.get('port')}")

config.set("debug", "true")
config.set("timeout", "30")
config.save_config()

# Example 3: File Backup Utility
def backup_file(source_filename, backup_dir="backups"):
    """Create a backup of a file"""
    import os
    from datetime import datetime
    
    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Generate backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{os.path.splitext(source_filename)[0]}_{timestamp}{os.path.splitext(source_filename)[1]}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    try:
        shutil.copy2(source_filename, backup_path)
        print(f"Backup created: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Error creating backup: {e}")
        return None

# Create backup of our sample file
backup_path = backup_file(filename)
if backup_path:
    print(f"Backup successful: {backup_path}")

# Cleanup created files
cleanup_files = [filename, data_file, csv_filename, json_filename, binary_filename, 
                log_filename, config_filename, "renamed_sample.txt"]
for file in cleanup_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"Cleaned up: {file}")

# Cleanup backup directory
if os.path.exists("backups"):
    shutil.rmtree("backups")
    print("Cleaned up backup directory")

# Exercises:
"""
1. Write a function that reads a text file and counts the number of words
2. Create a program that merges two CSV files
3. Write a function that finds and replaces text in a file
4. Create a program that logs user activities to a file
5. Write a function that compresses a text file by removing extra whitespace
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Word counter
print("Exercise 1: Word Counter")
def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return 0

# Create test file
test_file = "test.txt"
with open(test_file, "w") as file:
    file.write("This is a test file with multiple words.\n")
    file.write("It contains several lines of text.\n")
    file.write("Each line has different numbers of words.\n")

word_count = count_words(test_file)
print(f"Word count in '{test_file}': {word_count}")

# 2. CSV merger
print("\nExercise 2: CSV Merger")
def merge_csv_files(file1, file2, output_file):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as out:
            # Copy first file
            out.write(f1.read())
            # Skip header of second file and copy rest
            f2.readline()  # Skip header
            out.write(f2.read())
        print(f"Merged files into '{output_file}'")
    except FileNotFoundError as e:
        print(f"File not found: {e}")

# Create test CSV files
csv1 = "file1.csv"
csv2 = "file2.csv"
with open(csv1, "w") as file:
    file.write("Name,Age\nAlice,25\nBob,30\n")
with open(csv2, "w") as file:
    file.write("Name,Age\nCharlie,35\nDiana,28\n")

merge_csv_files(csv1, csv2, "merged.csv")

# 3. Find and replace
print("\nExercise 3: Find and Replace")
def find_replace_in_file(filename, old_text, new_text):
    try:
        with open(filename, "r") as file:
            content = file.read()
        
        updated_content = content.replace(old_text, new_text)
        
        with open(filename, "w") as file:
            file.write(updated_content)
        
        print(f"Replaced '{old_text}' with '{new_text}' in '{filename}'")
    except FileNotFoundError:
        print(f"File '{filename}' not found")

find_replace_in_file(test_file, "test", "sample")

# 4. Activity logger
print("\nExercise 4: Activity Logger")
class ActivityLogger:
    def __init__(self, log_file):
        self.log_file = log_file
    
    def log_activity(self, user, activity):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {user}: {activity}\n"
        
        with open(self.log_file, "a") as file:
            file.write(log_entry)
    
    def get_recent_activities(self, n=5):
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()
                return lines[-n:] if len(lines) >= n else lines
        except FileNotFoundError:
            return []

logger = ActivityLogger("activity.log")
logger.log_activity("Alice", "Logged in")
logger.log_activity("Bob", "Created new file")
logger.log_activity("Alice", "Updated profile")

recent = logger.get_recent_activities(3)
print("Recent activities:")
for activity in recent:
    print(f"  {activity.strip()}")

# 5. Text compressor
print("\nExercise 5: Text Compressor")
def compress_text_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        
        # Remove extra whitespace
        import re
        compressed = re.sub(r'\s+', ' ', content).strip()
        
        compressed_filename = f"compressed_{filename}"
        with open(compressed_filename, "w") as file:
            file.write(compressed)
        
        original_size = len(content)
        compressed_size = len(compressed)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f"Original size: {original_size} characters")
        print(f"Compressed size: {compressed_size} characters")
        print(f"Compression ratio: {compression_ratio:.1f}%")
        print(f"Compressed file saved as: {compressed_filename}")
        
    except FileNotFoundError:
        print(f"File '{filename}' not found")

compress_text_file(test_file)

# Cleanup
cleanup_files = [test_file, csv1, csv2, "merged.csv", "activity.log", "compressed_test.txt"]
for file in cleanup_files:
    if os.path.exists(file):
        os.remove(file)

print("\n🎉 Congratulations! You've completed Lesson 13!")
print("Next: Lesson 14 - Exception Handling")
