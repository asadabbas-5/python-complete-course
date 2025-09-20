# Lesson 20: Regular Expressions

"""
This lesson covers:
- Basic regex patterns and syntax
- Character classes and quantifiers
- Anchors and word boundaries
- Groups and capturing
- Lookahead and lookbehind
- Substitution and splitting
- Flags and modifiers
- Practical regex applications
"""

# 1. Basic Regex Patterns
print("=== Basic Regex Patterns ===")

import re

# Basic pattern matching
text = "Hello, World! Python is awesome."
pattern = r"Python"
match = re.search(pattern, text)

if match:
    print(f"Found '{match.group()}' at position {match.start()}-{match.end()}")
else:
    print("Pattern not found")

# Multiple matches
text = "The cat sat on the mat. The cat was happy."
pattern = r"cat"
matches = re.findall(pattern, text)
print(f"All matches: {matches}")

# Case-insensitive matching
text = "Python is great. PYTHON is powerful. python is versatile."
pattern = r"python"
matches = re.findall(pattern, text, re.IGNORECASE)
print(f"Case-insensitive matches: {matches}")

# 2. Character Classes and Quantifiers
print("\n=== Character Classes and Quantifiers ===")

# Character classes
text = "The quick brown fox jumps over the lazy dog."
pattern = r"[aeiou]"  # Vowels
vowels = re.findall(pattern, text)
print(f"Vowels: {vowels}")

# Quantifiers
text = "aaabbbcccdddeee"
pattern = r"a+"  # One or more 'a's
matches = re.findall(pattern, text)
print(f"One or more 'a's: {matches}")

pattern = r"a*"  # Zero or more 'a's
matches = re.findall(pattern, text)
print(f"Zero or more 'a's: {matches}")

pattern = r"a?"  # Zero or one 'a'
matches = re.findall(pattern, text)
print(f"Zero or one 'a': {matches}")

# Specific quantifiers
text = "a aa aaa aaaa aaaaa"
pattern = r"a{2,4}"  # 2 to 4 'a's
matches = re.findall(pattern, text)
print(f"2-4 'a's: {matches}")

# 3. Anchors and Word Boundaries
print("\n=== Anchors and Word Boundaries ===")

# Anchors
text = "Python is great. Python programming is fun."
pattern = r"^Python"  # Start of string
matches = re.findall(pattern, text)
print(f"Python at start: {matches}")

pattern = r"fun\.$"  # End of string
matches = re.findall(pattern, text)
print(f"fun at end: {matches}")

# Word boundaries
text = "The cat in the hat. Catastrophe. Scattered."
pattern = r"\bcat\b"  # Whole word 'cat'
matches = re.findall(pattern, text, re.IGNORECASE)
print(f"Whole word 'cat': {matches}")

# 4. Groups and Capturing
print("\n=== Groups and Capturing ===")

# Simple groups
text = "John Doe, Jane Smith, Bob Johnson"
pattern = r"(\w+)\s+(\w+)"  # First name and last name
matches = re.findall(pattern, text)
print(f"Name groups: {matches}")

# Named groups
text = "Email: john@example.com, Phone: 123-456-7890"
pattern = r"Email:\s+(?P<email>\S+),\s+Phone:\s+(?P<phone>[\d-]+)"
match = re.search(pattern, text)
if match:
    print(f"Email: {match.group('email')}")
    print(f"Phone: {match.group('phone')}")

# Non-capturing groups
text = "color colour"
pattern = r"colou?r"  # Match both 'color' and 'colour'
matches = re.findall(pattern, text)
print(f"Color variations: {matches}")

# 5. Lookahead and Lookbehind
print("\n=== Lookahead and Lookbehind ===")

# Positive lookahead
text = "Python3 Python2 Python"
pattern = r"Python(?=\d)"  # Python followed by a digit
matches = re.findall(pattern, text)
print(f"Python with version: {matches}")

# Negative lookahead
text = "Python3 Python2 Python"
pattern = r"Python(?!\d)"  # Python not followed by a digit
matches = re.findall(pattern, text)
print(f"Python without version: {matches}")

# Positive lookbehind
text = "Price: $100, Cost: $50, Value: $200"
pattern = r"(?<=\$)\d+"  # Digits preceded by $
matches = re.findall(pattern, text)
print(f"Prices: {matches}")

# Negative lookbehind
text = "Price: $100, Cost: 50, Value: $200"
pattern = r"(?<!\$)\d+"  # Digits not preceded by $
matches = re.findall(pattern, text)
print(f"Non-price numbers: {matches}")

# 6. Substitution and Splitting
print("\n=== Substitution and Splitting ===")

# Substitution
text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"
replacement = "cat"
new_text = re.sub(pattern, replacement, text)
print(f"Original: {text}")
print(f"Modified: {new_text}")

# Substitution with groups
text = "John Doe, Jane Smith, Bob Johnson"
pattern = r"(\w+)\s+(\w+)"
replacement = r"\2, \1"  # Last name, First name
new_text = re.sub(pattern, replacement, text)
print(f"Name format changed: {new_text}")

# Splitting
text = "apple,banana,cherry,date,elderberry"
pattern = r","
fruits = re.split(pattern, text)
print(f"Split fruits: {fruits}")

# Splitting with multiple delimiters
text = "apple,banana;cherry:date elderberry"
pattern = r"[,;:\s]+"
fruits = re.split(pattern, text)
print(f"Split with multiple delimiters: {fruits}")

# 7. Flags and Modifiers
print("\n=== Flags and Modifiers ===")

text = "Python is great.\nPYTHON is powerful.\npython is versatile."

# Case-insensitive flag
pattern = r"python"
matches = re.findall(pattern, text, re.IGNORECASE)
print(f"Case-insensitive matches: {matches}")

# Multiline flag
pattern = r"^python"
matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
print(f"Python at start of lines: {matches}")

# Dotall flag
text = "Start\nMiddle\nEnd"
pattern = r"Start.*End"
match = re.search(pattern, text, re.DOTALL)
if match:
    print(f"Multiline match: {match.group()}")

# Verbose flag for complex patterns
pattern = r"""
    \b          # Word boundary
    \d{3}       # Three digits
    -           # Hyphen
    \d{3}       # Three digits
    -           # Hyphen
    \d{4}       # Four digits
    \b          # Word boundary
"""
text = "Call me at 123-456-7890 or 987-654-3210"
matches = re.findall(pattern, text, re.VERBOSE)
print(f"Phone numbers: {matches}")

# 8. Common Regex Patterns
print("\n=== Common Regex Patterns ===")

# Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emails = ["user@example.com", "invalid-email", "test@domain.co.uk", "bad@email"]
for email in emails:
    is_valid = re.match(email_pattern, email)
    print(f"Email '{email}': {'Valid' if is_valid else 'Invalid'}")

# Phone number validation
phone_pattern = r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"
phones = ["123-456-7890", "(123) 456-7890", "123.456.7890", "123 456 7890"]
for phone in phones:
    match = re.match(phone_pattern, phone)
    if match:
        formatted = f"({match.group(1)}) {match.group(2)}-{match.group(3)}"
        print(f"Phone '{phone}' -> '{formatted}'")

# URL validation
url_pattern = r"^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$"
urls = ["https://www.example.com", "http://localhost:8080", "invalid-url"]
for url in urls:
    is_valid = re.match(url_pattern, url)
    print(f"URL '{url}': {'Valid' if is_valid else 'Invalid'}")

# 9. Advanced Regex Techniques
print("\n=== Advanced Regex Techniques ===")

# Backreferences
text = "The cat sat on the mat. The dog ran in the fog."
pattern = r"(\w+)\s+\1"  # Repeated words
matches = re.findall(pattern, text)
print(f"Repeated words: {matches}")

# Conditional patterns
text = "color colour"
pattern = r"colou?r"  # Optional 'u'
matches = re.findall(pattern, text)
print(f"Color/colour: {matches}")

# Recursive patterns (simplified)
text = "((hello))"
pattern = r"\(([^()]|\([^()]*\))*\)"  # Nested parentheses
matches = re.findall(pattern, text)
print(f"Nested parentheses: {matches}")

# 10. Practical Applications
print("\n=== Practical Applications ===")

# Application 1: Log Parser
class LogParser:
    """Parse log files with regex"""
    
    def __init__(self):
        self.log_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)"
    
    def parse_log_line(self, line):
        """Parse a single log line"""
        match = re.match(self.log_pattern, line)
        if match:
            timestamp, level, message = match.groups()
            return {
                'timestamp': timestamp,
                'level': level,
                'message': message
            }
        return None
    
    def extract_errors(self, log_lines):
        """Extract error messages from log"""
        errors = []
        for line in log_lines:
            parsed = self.parse_log_line(line)
            if parsed and parsed['level'] == 'ERROR':
                errors.append(parsed)
        return errors

# Test log parser
log_parser = LogParser()
log_lines = [
    "2024-01-15 10:00:00 [INFO] Application started",
    "2024-01-15 10:05:00 [ERROR] Database connection failed",
    "2024-01-15 10:10:00 [WARNING] High memory usage",
    "2024-01-15 10:15:00 [ERROR] File not found"
]

errors = log_parser.extract_errors(log_lines)
print(f"Found {len(errors)} errors")

# Application 2: Data Extractor
class DataExtractor:
    """Extract structured data from text"""
    
    def __init__(self):
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            'url': r'https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?)?',
            'ip': r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        }
    
    def extract_all(self, text):
        """Extract all supported data types"""
        results = {}
        for data_type, pattern in self.patterns.items():
            matches = re.findall(pattern, text)
            results[data_type] = matches
        return results

# Test data extractor
extractor = DataExtractor()
sample_text = """
Contact us at john@example.com or call 123-456-7890.
Visit our website at https://www.example.com.
Our server IP is 192.168.1.1.
"""

extracted = extractor.extract_all(sample_text)
for data_type, matches in extracted.items():
    print(f"{data_type.title()}: {matches}")

# Application 3: Text Processor
class TextProcessor:
    """Process text with regex operations"""
    
    def clean_text(self, text):
        """Clean text by removing extra whitespace and special characters"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters except basic punctuation
        text = re.sub(r'[^\w\s.,!?]', '', text)
        return text.strip()
    
    def extract_sentences(self, text):
        """Extract sentences from text"""
        pattern = r'[.!?]+'
        sentences = re.split(pattern, text)
        return [s.strip() for s in sentences if s.strip()]
    
    def extract_words(self, text):
        """Extract words from text"""
        pattern = r'\b\w+\b'
        return re.findall(pattern, text.lower())
    
    def count_word_frequency(self, text):
        """Count word frequency in text"""
        words = self.extract_words(text)
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

# Test text processor
processor = TextProcessor()
sample_text = "Hello, world! How are you? I'm doing great. Hello again!"

cleaned = processor.clean_text(sample_text)
sentences = processor.extract_sentences(sample_text)
words = processor.extract_words(sample_text)
word_freq = processor.count_word_frequency(sample_text)

print(f"Cleaned text: {cleaned}")
print(f"Sentences: {sentences}")
print(f"Words: {words}")
print(f"Word frequency: {word_freq}")

# 11. Performance Considerations
print("\n=== Performance Considerations ===")

import time

# Compile regex patterns for better performance
text = "The quick brown fox jumps over the lazy dog. " * 1000

# Without compilation
start_time = time.time()
for _ in range(1000):
    re.search(r"fox", text)
no_compile_time = time.time() - start_time

# With compilation
compiled_pattern = re.compile(r"fox")
start_time = time.time()
for _ in range(1000):
    compiled_pattern.search(text)
compile_time = time.time() - start_time

print(f"Without compilation: {no_compile_time:.4f}s")
print(f"With compilation: {compile_time:.4f}s")
print(f"Performance improvement: {no_compile_time/compile_time:.2f}x")

# 12. Best Practices
print("\n=== Best Practices ===")

# Best Practice 1: Use raw strings for regex patterns
pattern = r"\d+"  # Good
# pattern = "\\d+"  # Bad - requires escaping

# Best Practice 2: Compile patterns for repeated use
compiled_email = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# Best Practice 3: Use appropriate flags
text = "Python is great.\nPYTHON is powerful."
pattern = r"^python"
matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)

# Best Practice 4: Handle regex errors gracefully
def safe_regex_search(pattern, text):
    try:
        return re.search(pattern, text)
    except re.error as e:
        print(f"Regex error: {e}")
        return None

# Best Practice 5: Use verbose mode for complex patterns
complex_pattern = re.compile(r"""
    ^
    (?P<username>[a-zA-Z0-9._%+-]+)
    @
    (?P<domain>[a-zA-Z0-9.-]+)
    \.
    (?P<tld>[a-zA-Z]{2,})
    $
""", re.VERBOSE)

# Exercises:
"""
1. Write a regex pattern to match valid email addresses
2. Create a regex pattern to extract phone numbers in various formats
3. Write a regex pattern to find all words that start with a capital letter
4. Create a regex pattern to match dates in MM/DD/YYYY format
5. Write a regex pattern to extract all URLs from a text
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Email validation
print("Exercise 1: Email Validation")
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
test_emails = ["user@example.com", "test.email@domain.co.uk", "invalid-email", "user@domain"]
for email in test_emails:
    is_valid = re.match(email_pattern, email)
    print(f"'{email}': {'Valid' if is_valid else 'Invalid'}")

# 2. Phone number extraction
print("\nExercise 2: Phone Number Extraction")
phone_pattern = r"\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})"
text = "Call me at 123-456-7890 or (987) 654-3210 or 555.123.4567"
matches = re.findall(phone_pattern, text)
print(f"Phone numbers found: {matches}")

# 3. Capital letter words
print("\nExercise 3: Capital Letter Words")
text = "The Quick Brown Fox jumps over the Lazy Dog"
pattern = r"\b[A-Z][a-z]*\b"
matches = re.findall(pattern, text)
print(f"Capital letter words: {matches}")

# 4. Date matching
print("\nExercise 4: Date Matching")
date_pattern = r"\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}\b"
text = "Today is 01/15/2024 and tomorrow is 01/16/2024"
matches = re.findall(date_pattern, text)
print(f"Dates found: {matches}")

# 5. URL extraction
print("\nExercise 5: URL Extraction")
url_pattern = r"https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?)?"
text = "Visit https://www.example.com or http://localhost:8080 for more info"
matches = re.findall(url_pattern, text)
print(f"URLs found: {matches}")

print("\n🎉 Congratulations! You've completed Lesson 20!")
print("Next: Lesson 21 - Decorators")
