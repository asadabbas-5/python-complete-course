# Lesson 30: Database Programming

"""
This lesson covers:
- Database concepts
- SQLite database
- Database connections
- CRUD operations
- SQL queries
- Database transactions
- Error handling
- Database design
- ORM (Object-Relational Mapping)
- Practical database examples
"""

# 1. Database Concepts
print("=== Database Concepts ===")

# Database is a collection of organized data
# SQL (Structured Query Language) is used to interact with databases

import sqlite3
import os

print("Database concepts:")
print("- Table: Collection of related data")
print("- Row: Individual record in a table")
print("- Column: Field in a table")
print("- Primary Key: Unique identifier for each row")
print("- Foreign Key: Reference to another table")

# 2. SQLite Database
print("\n=== SQLite Database ===")

# SQLite is a lightweight, file-based database
# Perfect for learning and small applications

def create_database():
    # Create or connect to database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database and table created successfully")

create_database()

# 3. Database Connections
print("\n=== Database Connections ===")

def database_connection_example():
    # Connect to database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    try:
        # Database operations
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"Tables in database: {tables}")
        
    finally:
        # Always close connection
        conn.close()
        print("Database connection closed")

database_connection_example()

# 4. CRUD Operations
print("\n=== CRUD Operations ===")

# CREATE - Insert data
def create_operations():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Insert single record
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                   ("Alice", "alice@example.com", 25))
    
    # Insert multiple records
    users_data = [
        ("Bob", "bob@example.com", 30),
        ("Charlie", "charlie@example.com", 35),
        ("Diana", "diana@example.com", 28)
    ]
    cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users_data)
    
    conn.commit()
    conn.close()
    print("Records created successfully")

create_operations()

# READ - Select data
def read_operations():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Select all records
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    print("All users:")
    for user in all_users:
        print(f"  {user}")
    
    # Select specific records
    cursor.execute("SELECT name, email FROM users WHERE age > 25")
    filtered_users = cursor.fetchall()
    print("\nUsers older than 25:")
    for user in filtered_users:
        print(f"  {user}")
    
    # Select single record
    cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
    alice = cursor.fetchone()
    print(f"\nAlice's record: {alice}")
    
    conn.close()

read_operations()

# UPDATE - Modify data
def update_operations():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Update single record
    cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
    
    # Update multiple records
    cursor.execute("UPDATE users SET age = age + 1 WHERE age < 30")
    
    conn.commit()
    conn.close()
    print("Records updated successfully")

update_operations()

# DELETE - Remove data
def delete_operations():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Delete specific record
    cursor.execute("DELETE FROM users WHERE name = ?", ("Diana",))
    
    # Delete multiple records
    cursor.execute("DELETE FROM users WHERE age > 35")
    
    conn.commit()
    conn.close()
    print("Records deleted successfully")

delete_operations()

# 5. SQL Queries
print("\n=== SQL Queries ===")

def sql_queries_example():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Complex queries
    cursor.execute("""
        SELECT name, email, age 
        FROM users 
        WHERE age BETWEEN 25 AND 35 
        ORDER BY age DESC
    """)
    results = cursor.fetchall()
    print("Users aged 25-35, ordered by age:")
    for user in results:
        print(f"  {user}")
    
    # Aggregate functions
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"\nTotal users: {count}")
    
    cursor.execute("SELECT AVG(age) FROM users")
    avg_age = cursor.fetchone()[0]
    print(f"Average age: {avg_age:.2f}")
    
    cursor.execute("SELECT MAX(age), MIN(age) FROM users")
    max_min = cursor.fetchone()
    print(f"Age range: {max_min[1]} - {max_min[0]}")
    
    conn.close()

sql_queries_example()

# 6. Database Transactions
print("\n=== Database Transactions ===")

def transaction_example():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    try:
        # Begin transaction
        cursor.execute("BEGIN TRANSACTION")
        
        # Multiple operations
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                       ("Eve", "eve@example.com", 22))
        cursor.execute("UPDATE users SET age = age + 1 WHERE name = 'Alice'")
        
        # Commit transaction
        conn.commit()
        print("Transaction committed successfully")
        
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print(f"Transaction rolled back: {e}")
    
    finally:
        conn.close()

transaction_example()

# 7. Error Handling
print("\n=== Error Handling ===")

def error_handling_example():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    try:
        # This will cause an error (duplicate email)
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                       ("Alice", "alice@example.com", 25))
        conn.commit()
        
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
    finally:
        conn.close()

error_handling_example()

# 8. Database Design
print("\n=== Database Design ===")

def database_design_example():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create related tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product TEXT,
            quantity INTEGER,
            price REAL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Insert sample data
    cursor.execute("INSERT INTO orders (user_id, product, quantity, price) VALUES (?, ?, ?, ?)", 
                   (1, "Laptop", 1, 999.99))
    cursor.execute("INSERT INTO orders (user_id, product, quantity, price) VALUES (?, ?, ?, ?)", 
                   (2, "Mouse", 2, 25.50))
    
    # Join query
    cursor.execute("""
        SELECT u.name, o.product, o.quantity, o.price
        FROM users u
        JOIN orders o ON u.id = o.user_id
    """)
    
    results = cursor.fetchall()
    print("User orders:")
    for result in results:
        print(f"  {result}")
    
    conn.commit()
    conn.close()

database_design_example()

# 9. ORM (Object-Relational Mapping)
print("\n=== ORM (Object-Relational Mapping) ===")

# Simple ORM implementation
class SimpleORM:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def create_table(self, table_name, columns):
        columns_str = ", ".join([f"{col} {type}" for col, type in columns.items()])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})")
        self.conn.commit()
    
    def insert(self, table_name, data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, list(data.values()))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def select(self, table_name, where=None):
        query = f"SELECT * FROM {table_name}"
        if where:
            query += f" WHERE {where}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def update(self, table_name, data, where):
        set_clause = ", ".join([f"{col} = ?" for col in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
        self.cursor.execute(query, list(data.values()))
        self.conn.commit()
    
    def delete(self, table_name, where):
        query = f"DELETE FROM {table_name} WHERE {where}"
        self.cursor.execute(query)
        self.conn.commit()
    
    def close(self):
        self.conn.close()

# Use SimpleORM
def orm_example():
    orm = SimpleORM('orm_example.db')
    
    # Create table
    orm.create_table('products', {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'name': 'TEXT NOT NULL',
        'price': 'REAL',
        'category': 'TEXT'
    })
    
    # Insert data
    product_id = orm.insert('products', {
        'name': 'Python Book',
        'price': 29.99,
        'category': 'Books'
    })
    print(f"Inserted product with ID: {product_id}")
    
    # Select data
    products = orm.select('products')
    print(f"Products: {products}")
    
    # Update data
    orm.update('products', {'price': 24.99}, f"id = {product_id}")
    
    # Select updated data
    products = orm.select('products')
    print(f"Updated products: {products}")
    
    orm.close()

orm_example()

# 10. Practical Database Examples
print("\n=== Practical Database Examples ===")

# Example 1: User Management System
def user_management_system():
    conn = sqlite3.connect('user_management.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    
    # Insert sample users
    users = [
        ("alice", "alice@example.com", "hash1"),
        ("bob", "bob@example.com", "hash2"),
        ("charlie", "charlie@example.com", "hash3")
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        users
    )
    
    # User operations
    def create_user(username, email, password_hash):
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        return cursor.lastrowid
    
    def get_user(username):
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()
    
    def update_user_status(username, is_active):
        cursor.execute(
            "UPDATE users SET is_active = ? WHERE username = ?",
            (is_active, username)
        )
    
    def delete_user(username):
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    
    # Test operations
    print("User Management System:")
    
    # Get all users
    cursor.execute("SELECT username, email, is_active FROM users")
    users = cursor.fetchall()
    print("All users:")
    for user in users:
        print(f"  {user}")
    
    # Get specific user
    alice = get_user("alice")
    print(f"\nAlice's info: {alice}")
    
    # Update user status
    update_user_status("bob", 0)
    print("\nUpdated Bob's status to inactive")
    
    conn.commit()
    conn.close()

user_management_system()

# Example 2: Inventory Management
def inventory_management():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL,
            stock_quantity INTEGER DEFAULT 0,
            min_stock_level INTEGER DEFAULT 5,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert sample products
    products = [
        ("Laptop", "Electronics", 999.99, 10, 2),
        ("Mouse", "Electronics", 25.50, 50, 10),
        ("Keyboard", "Electronics", 75.00, 30, 5),
        ("Book", "Education", 29.99, 100, 20)
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO products (name, category, price, stock_quantity, min_stock_level) VALUES (?, ?, ?, ?, ?)",
        products
    )
    
    # Inventory operations
    def add_stock(product_id, quantity):
        cursor.execute(
            "UPDATE products SET stock_quantity = stock_quantity + ? WHERE id = ?",
            (quantity, product_id)
        )
    
    def remove_stock(product_id, quantity):
        cursor.execute(
            "UPDATE products SET stock_quantity = stock_quantity - ? WHERE id = ?",
            (quantity, product_id)
        )
    
    def check_low_stock():
        cursor.execute(
            "SELECT name, stock_quantity, min_stock_level FROM products WHERE stock_quantity <= min_stock_level"
        )
        return cursor.fetchall()
    
    def get_inventory_value():
        cursor.execute("SELECT SUM(price * stock_quantity) FROM products")
        return cursor.fetchone()[0]
    
    # Test operations
    print("\nInventory Management:")
    
    # Check low stock
    low_stock = check_low_stock()
    print("Low stock items:")
    for item in low_stock:
        print(f"  {item}")
    
    # Add stock
    add_stock(1, 5)  # Add 5 laptops
    print("\nAdded 5 laptops to stock")
    
    # Get inventory value
    total_value = get_inventory_value()
    print(f"Total inventory value: ${total_value:.2f}")
    
    conn.commit()
    conn.close()

inventory_management()

# Example 3: Library Management System
def library_management_system():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE,
            available_copies INTEGER DEFAULT 1,
            total_copies INTEGER DEFAULT 1
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            membership_date DATE DEFAULT CURRENT_DATE
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            loan_date DATE DEFAULT CURRENT_DATE,
            return_date DATE,
            due_date DATE,
            FOREIGN KEY (book_id) REFERENCES books (id),
            FOREIGN KEY (member_id) REFERENCES members (id)
        )
    ''')
    
    # Insert sample data
    books = [
        ("Python Programming", "John Doe", "978-1234567890", 3, 3),
        ("Data Science", "Jane Smith", "978-0987654321", 2, 2),
        ("Machine Learning", "Bob Johnson", "978-1122334455", 1, 1)
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO books (title, author, isbn, available_copies, total_copies) VALUES (?, ?, ?, ?, ?)",
        books
    )
    
    members = [
        ("Alice Brown", "alice@example.com", "555-0101"),
        ("Charlie Davis", "charlie@example.com", "555-0102")
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO members (name, email, phone) VALUES (?, ?, ?)",
        members
    )
    
    # Library operations
    def borrow_book(book_id, member_id):
        # Check if book is available
        cursor.execute("SELECT available_copies FROM books WHERE id = ?", (book_id,))
        available = cursor.fetchone()[0]
        
        if available > 0:
            # Update available copies
            cursor.execute(
                "UPDATE books SET available_copies = available_copies - 1 WHERE id = ?",
                (book_id,)
            )
            
            # Create loan record
            cursor.execute(
                "INSERT INTO loans (book_id, member_id, due_date) VALUES (?, ?, date('now', '+14 days'))",
                (book_id, member_id)
            )
            return True
        return False
    
    def return_book(loan_id):
        # Get loan details
        cursor.execute("SELECT book_id FROM loans WHERE id = ?", (loan_id,))
        book_id = cursor.fetchone()[0]
        
        # Update available copies
        cursor.execute(
            "UPDATE books SET available_copies = available_copies + 1 WHERE id = ?",
            (book_id,)
        )
        
        # Update loan record
        cursor.execute(
            "UPDATE loans SET return_date = CURRENT_DATE WHERE id = ?",
            (loan_id,)
        )
    
    def get_overdue_loans():
        cursor.execute("""
            SELECT l.id, b.title, m.name, l.due_date
            FROM loans l
            JOIN books b ON l.book_id = b.id
            JOIN members m ON l.member_id = m.id
            WHERE l.return_date IS NULL AND l.due_date < CURRENT_DATE
        """)
        return cursor.fetchall()
    
    # Test operations
    print("\nLibrary Management System:")
    
    # Borrow a book
    if borrow_book(1, 1):  # Alice borrows Python Programming
        print("Alice borrowed Python Programming")
    
    # Check overdue loans
    overdue = get_overdue_loans()
    print(f"Overdue loans: {len(overdue)}")
    
    # Get all books with availability
    cursor.execute("SELECT title, available_copies, total_copies FROM books")
    books_info = cursor.fetchall()
    print("\nBooks availability:")
    for book in books_info:
        print(f"  {book}")
    
    conn.commit()
    conn.close()

library_management_system()

# Cleanup
def cleanup_databases():
    db_files = ['example.db', 'orm_example.db', 'user_management.db', 'inventory.db', 'library.db']
    for db_file in db_files:
        if os.path.exists(db_file):
            os.remove(db_file)
            print(f"Removed {db_file}")

cleanup_databases()

print("\n🎉 Congratulations! You've completed Lesson 30!")
print("You've completed the Advanced Level of Python programming!")
print("Next: Professional Level - Testing, Deployment, and Best Practices")
