# Lesson 10: String Methods

"""
This lesson covers:
- String creation and basic operations
- String methods for manipulation
- String formatting and interpolation
- Regular expressions basics
- String validation and cleaning
- Common string patterns and best practices
"""

# 1. String Creation and Basic Operations
print("=== String Creation and Basic Operations ===")

# Creating strings
single_quote = 'Hello, World!'
double_quote = "Hello, World!"
triple_quote = """This is a
multiline string"""

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Triple quote: {triple_quote}")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition
repeated = "Python " * 3
print(f"Repeated: {repeated}")

# String length
text = "Hello, World!"
print(f"Length of '{text}': {len(text)}")

# 2. String Indexing and Slicing
print("\n=== String Indexing and Slicing ===")

text = "Python Programming"
print(f"Original text: {text}")

# Indexing
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Character at index 6: {text[6]}")

# Slicing
print(f"First 6 characters: {text[:6]}")
print(f"Last 11 characters: {text[-11:]}")
print(f"Characters 7-11: {text[7:12]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reverse: {text[::-1]}")

# 3. String Methods - Case Manipulation
print("\n=== String Methods - Case Manipulation ===")

text = "Hello World Python"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Swap case: {text.swapcase()}")

# Case checking
print(f"Is upper: {text.isupper()}")
print(f"Is lower: {text.islower()}")
print(f"Is title: {text.istitle()}")

# 4. String Methods - Whitespace and Alignment
print("\n=== String Methods - Whitespace and Alignment ===")

text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Lstrip: '{text.lstrip()}'")
print(f"Rstrip: '{text.rstrip()}'")

# Padding
text = "Hello"
print(f"Original: '{text}'")
print(f"Center (10): '{text.center(10)}'")
print(f"Ljust (10): '{text.ljust(10)}'")
print(f"Rjust (10): '{text.rjust(10)}'")
print(f"Zfill (8): '{text.zfill(8)}'")

# 5. String Methods - Searching and Checking
print("\n=== String Methods - Searching and Checking ===")

text = "Python is awesome and Python is powerful"
print(f"Text: {text}")

# Finding substrings
print(f"Find 'Python': {text.find('Python')}")
print(f"Find 'Java': {text.find('Java')}")  # Returns -1 if not found
print(f"Rfind 'Python': {text.rfind('Python')}")
print(f"Index 'Python': {text.index('Python')}")

# Counting occurrences
print(f"Count 'Python': {text.count('Python')}")
print(f"Count 'is': {text.count('is')}")

# Checking content
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'powerful': {text.endswith('powerful')}")

# Character type checking
sample_text = "Hello123"
print(f"'{sample_text}' is alphanumeric: {sample_text.isalnum()}")
print(f"'{sample_text}' is alphabetic: {sample_text.isalpha()}")
print(f"'{sample_text}' is numeric: {sample_text.isdigit()}")
print(f"'{sample_text}' is decimal: {sample_text.isdecimal()}")

# 6. String Methods - Splitting and Joining
print("\n=== String Methods - Splitting and Joining ===")

# Splitting
text = "apple,banana,cherry,date"
print(f"Original: {text}")
print(f"Split by comma: {text.split(',')}")
print(f"Split by comma (max 2): {text.split(',', 2)}")

# Splitting lines
multiline_text = "Line 1\nLine 2\nLine 3"
print(f"Multiline text:\n{multiline_text}")
print(f"Split lines: {multiline_text.splitlines()}")

# Joining
fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}")
print(f"Joined with comma: {','.join(fruits)}")
print(f"Joined with space: {' '.join(fruits)}")
print(f"Joined with newline:\n{chr(10).join(fruits)}")

# 7. String Methods - Replacement and Translation
print("\n=== String Methods - Replacement and Translation ===")

text = "Hello World Hello Python"
print(f"Original: {text}")

# Replace
print(f"Replace 'Hello' with 'Hi': {text.replace('Hello', 'Hi')}")
print(f"Replace first 'Hello' only: {text.replace('Hello', 'Hi', 1)}")

# Translation table
translation_table = str.maketrans('aeiou', '12345')
text_to_translate = "hello world"
print(f"Original: {text_to_translate}")
print(f"Translated: {text_to_translate.translate(translation_table)}")

# 8. String Formatting Methods
print("\n=== String Formatting Methods ===")

name = "Alice"
age = 25
height = 5.6

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}, Height: {height}")

# .format() method
print("Name: {}, Age: {}, Height: {}".format(name, age, height))
print("Name: {0}, Age: {1}, Height: {2}".format(name, age, height))
print("Name: {n}, Age: {a}, Height: {h}".format(n=name, a=age, h=height))

# % formatting (older style)
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

# Advanced formatting
pi = 3.14159
print(f"Pi: {pi:.2f}")
print(f"Pi: {pi:.4f}")
print(f"Pi: {pi:e}")
print(f"Pi: {pi:.2%}")

# 9. String Validation and Cleaning
print("\n=== String Validation and Cleaning ===")

def clean_string(text):
    """Clean and validate a string"""
    if not isinstance(text, str):
        return None
    
    # Remove extra whitespace
    cleaned = text.strip()
    
    # Remove multiple spaces
    import re
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    return cleaned

def validate_email(email):
    """Basic email validation"""
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local, domain = parts
    if not local or not domain or '.' not in domain:
        return False
    
    return True

# Test validation functions
test_strings = ["  hello   world  ", "normal text", "multiple    spaces"]
for text in test_strings:
    cleaned = clean_string(text)
    print(f"'{text}' -> '{cleaned}'")

test_emails = ["user@example.com", "invalid-email", "user@domain", ""]
for email in test_emails:
    is_valid = validate_email(email)
    print(f"'{email}' is valid: {is_valid}")

# 10. Regular Expressions Basics
print("\n=== Regular Expressions Basics ===")

import re

text = "Contact us at support@example.com or call 123-456-7890"

# Finding patterns
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print(f"Text: {text}")
print(f"Found emails: {emails}")
print(f"Found phones: {phones}")

# Substitution
masked_text = re.sub(phone_pattern, 'XXX-XXX-XXXX', text)
print(f"Masked text: {masked_text}")

# Splitting with regex
text_to_split = "apple,banana;cherry:date"
split_result = re.split(r'[,;:]', text_to_split)
print(f"Split result: {split_result}")

# 11. Common String Patterns
print("\n=== Common String Patterns ===")

# Pattern 1: Palindrome check
def is_palindrome(text):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

test_words = ["racecar", "hello", "A man a plan a canal Panama"]
for word in test_words:
    print(f"'{word}' is palindrome: {is_palindrome(word)}")

# Pattern 2: Word frequency
def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "Python is great. Python is awesome. Python is powerful."
freq = word_frequency(text)
print(f"Word frequency: {freq}")

# Pattern 3: Text cleaning
def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters except basic punctuation
    text = re.sub(r'[^\w\s.,!?]', '', text)
    return text.strip()

dirty_text = "  Hello!!!   World...   How are you???   "
clean = clean_text(dirty_text)
print(f"Dirty: '{dirty_text}'")
print(f"Clean: '{clean}'")

# 12. Practical Examples
print("\n=== Practical Examples ===")

# Example 1: Text Analyzer
class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = self._extract_words()
    
    def _extract_words(self):
        return re.findall(r'\b\w+\b', self.text.lower())
    
    def word_count(self):
        return len(self.words)
    
    def unique_word_count(self):
        return len(set(self.words))
    
    def most_common_words(self, n=5):
        word_count = {}
        for word in self.words:
            word_count[word] = word_count.get(word, 0) + 1
        
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]
    
    def average_word_length(self):
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return total_length / len(self.words)
    
    def sentence_count(self):
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])

# Test text analyzer
sample_text = "Python is a great programming language. Python is easy to learn. Python is powerful and versatile."
analyzer = TextAnalyzer(sample_text)

print(f"Text: {sample_text}")
print(f"Word count: {analyzer.word_count()}")
print(f"Unique words: {analyzer.unique_word_count()}")
print(f"Most common words: {analyzer.most_common_words()}")
print(f"Average word length: {analyzer.average_word_length():.2f}")
print(f"Sentence count: {analyzer.sentence_count()}")

# Example 2: Password Validator
class PasswordValidator:
    def __init__(self):
        self.requirements = {
            'min_length': 8,
            'max_length': 128,
            'require_uppercase': True,
            'require_lowercase': True,
            'require_digits': True,
            'require_special': True
        }
    
    def validate(self, password):
        errors = []
        
        if len(password) < self.requirements['min_length']:
            errors.append(f"Password must be at least {self.requirements['min_length']} characters long")
        
        if len(password) > self.requirements['max_length']:
            errors.append(f"Password must be no more than {self.requirements['max_length']} characters long")
        
        if self.requirements['require_uppercase'] and not re.search(r'[A-Z]', password):
            errors.append("Password must contain at least one uppercase letter")
        
        if self.requirements['require_lowercase'] and not re.search(r'[a-z]', password):
            errors.append("Password must contain at least one lowercase letter")
        
        if self.requirements['require_digits'] and not re.search(r'\d', password):
            errors.append("Password must contain at least one digit")
        
        if self.requirements['require_special'] and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("Password must contain at least one special character")
        
        return len(errors) == 0, errors

# Test password validator
validator = PasswordValidator()
test_passwords = ["weak", "Strong123", "MyPassword123!", "12345678"]

for password in test_passwords:
    is_valid, errors = validator.validate(password)
    print(f"'{password}': {'Valid' if is_valid else 'Invalid'}")
    if errors:
        for error in errors:
            print(f"  - {error}")

# 13. Performance Tips
print("\n=== Performance Tips ===")

# Tip 1: Use f-strings for formatting (fastest)
# Tip 2: Use join() for concatenating multiple strings
# Tip 3: Use strip() methods instead of manual whitespace removal
# Tip 4: Compile regex patterns if used repeatedly

# Example of compiled regex
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
text = "Contact us at support@example.com"
matches = email_pattern.findall(text)
print(f"Compiled regex matches: {matches}")

# Exercises:
"""
1. Write a function that reverses a string
2. Create a function that counts vowels in a string
3. Write a program that removes all punctuation from a string
4. Create a function that capitalizes the first letter of each word
5. Write a program that finds the longest word in a sentence
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Reverse string
print("Exercise 1: Reverse String")
def reverse_string(text):
    return text[::-1]

text = "Hello World"
reversed_text = reverse_string(text)
print(f"'{text}' reversed: '{reversed_text}'")

# 2. Count vowels
print("\nExercise 2: Count Vowels")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "Hello World"
vowel_count = count_vowels(text)
print(f"Vowels in '{text}': {vowel_count}")

# 3. Remove punctuation
print("\nExercise 3: Remove Punctuation")
def remove_punctuation(text):
    import re
    return re.sub(r'[^\w\s]', '', text)

text = "Hello, World! How are you?"
clean_text = remove_punctuation(text)
print(f"'{text}' without punctuation: '{clean_text}'")

# 4. Capitalize words
print("\nExercise 4: Capitalize Words")
def capitalize_words(text):
    return text.title()

text = "hello world python programming"
capitalized = capitalize_words(text)
print(f"'{text}' capitalized: '{capitalized}'")

# 5. Longest word
print("\nExercise 5: Longest Word")
def longest_word(sentence):
    words = sentence.split()
    if not words:
        return None
    return max(words, key=len)

sentence = "Python is a great programming language"
longest = longest_word(sentence)
print(f"Longest word in '{sentence}': '{longest}'")

print("\n🎉 Congratulations! You've completed Lesson 10!")
print("Next: Lesson 11 - Functions")
