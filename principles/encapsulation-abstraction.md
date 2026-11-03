# 🏗️ Encapsulation & Abstraction: Managing Complexity

## Introduction

As programs grow, complexity increases. **Encapsulation** and **abstraction** are two powerful principles that help us manage that complexity by:
- **Hiding implementation details** - Users don't need to know how things work internally
- **Exposing only what's necessary** - A clean, simple interface
- **Changing internals safely** - Users aren't affected by internal changes
- **Organizing code logically** - Related data and methods stay together

Think of it like a car: you don't need to understand the engine's combustion mechanics to drive it. The steering wheel, pedals, and gear shift are the **interface**. The engine internals are **encapsulated**.

## Encapsulation: Hiding Internal State

Encapsulation means keeping data **private** and exposing it only through controlled **methods**.

### Without Encapsulation (Bad)

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance  # Public! Anyone can change it

# Usage
account = BankAccount("123456", 1000)
print(account.balance)  # 1000

# Oops! Direct manipulation
account.balance = -5000  # Now the account has negative balance!
```

**Problems:**
- Anyone can set balance to invalid values (negative, wrong type, etc.)
- No record of who changed it or when
- Business logic can be bypassed

### With Encapsulation (Good)

```python
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Private (double underscore)
        self.__balance = initial_balance        # Private
    
    # Controlled access to read balance
    def get_balance(self):
        return self.__balance
    
    # Controlled withdrawal with validation
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")
    
    # Controlled deposit with validation
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

# Usage
account = BankAccount("123456", 1000)
print(account.get_balance())  # 1000

# Can't directly modify balance anymore
# account.__balance = -5000  # AttributeError!

# Must use methods with validation
account.withdraw(100)  # Withdrawal validated
account.deposit(-50)   # ValueError: Deposit amount must be positive
```

**Benefits:**
- Balance can only be changed through validated methods
- Business rules are enforced
- Internal representation can change without affecting users

### Levels of Access Control

Different languages provide different access levels:

**Python (by convention):**
```python
class Example:
    def public_method(self):          # Anyone can call
        pass
    
    def _protected_method(self):      # Discouraged but possible (single underscore)
        pass
    
    def __private_method(self):       # Name-mangled, strongly discouraged (double underscore)
        pass
```

**SQL (for tables):**
- Views with restricted columns: Users see only what they need
- Stored procedures: Users call procedures, not raw table operations

## Abstraction: Simplifying Interfaces

Abstraction means exposing **only essential features**, hiding complexity behind a simple interface.

### Abstraction Example 1: Collections

**Without abstraction, you'd write:**
```python
# Manual list implementation
items = []
items.append(1)
items.append(2)
idx = 0
while idx < len(items):
    print(items[idx])
    idx += 1
```

**With abstraction (using the list interface):**
```python
items = []
items.append(1)
items.append(2)
for item in items:
    print(item)
```

The list class **abstracts away** the internal details of storage and iteration. You just use simple methods: `append()`, `pop()`, etc.

### Abstraction Example 2: Database Connection

**Without abstraction:**
```python
# You'd manually handle sockets, protocols, parsing
socket = create_socket()
socket.connect("database.example.com", 5432)
socket.send(b"SELECT * FROM users;")
response = socket.receive()
# Parse binary response manually...
```

**With abstraction (using a database library):**
```python
import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
```

The library **abstracts away** network protocols, parsing, and connection management.

### Abstraction Example 3: Building a High-Level API

```python
# Low-level details of weather data retrieval
class WeatherDataReader:
    def __init__(self, data_source):
        self.data_source = data_source
    
    def fetch_raw_bytes(self):
        """Internal: fetch raw data from source."""
        # Complex HTTP request, parsing, error handling
        pass
    
    def parse_bytes_to_dict(self, data):
        """Internal: convert bytes to structured data."""
        # Complex parsing logic
        pass
    
    def validate_data(self, data):
        """Internal: ensure data integrity."""
        # Validation logic
        pass

# High-level abstraction
class Weather:
    def __init__(self, location):
        self.reader = WeatherDataReader(f"api.weather.com/{location}")
    
    def get_temperature(self):
        """Simple interface for temperature."""
        raw = self.reader.fetch_raw_bytes()
        data = self.reader.parse_bytes_to_dict(raw)
        self.reader.validate_data(data)
        return data['temperature']
    
    def get_forecast(self):
        """Simple interface for forecast."""
        raw = self.reader.fetch_raw_bytes()
        data = self.reader.parse_bytes_to_dict(raw)
        self.reader.validate_data(data)
        return data['forecast']

# User code
weather = Weather("New York")
print(weather.get_temperature())  # Simple!
# Users don't care about HTTP, parsing, validation
```

## Combining Encapsulation and Abstraction

The best designs combine both:

```python
class User:
    """Represents a user with private state and simple public interface."""
    
    def __init__(self, username, password):
        # Encapsulation: keep internal state private
        self.__username = username
        self.__password = self.__hash_password(password)
        self.__created_at = datetime.now()
    
    # Abstraction: simple public interface
    def verify_password(self, password):
        """Check if provided password is correct."""
        return self.__compare_hashes(self.__hash_password(password), self.__password)
    
    def get_username(self):
        """Get the username."""
        return self.__username
    
    def change_password(self, old_password, new_password):
        """Change password with verification."""
        if not self.verify_password(old_password):
            raise ValueError("Old password is incorrect")
        self.__password = self.__hash_password(new_password)
    
    # Encapsulation: private helper methods
    def __hash_password(self, password):
        """Internal: hash password securely."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def __compare_hashes(self, hash1, hash2):
        """Internal: compare password hashes."""
        return hash1 == hash2

# Usage
user = User("alice", "secret123")
user.verify_password("secret123")  # True
user.verify_password("wrong")      # False
user.change_password("secret123", "newsecret")
# Can't access internal __password
```

## Abstraction in SQL

**Without abstraction (raw tables):**
```sql
-- Users must write complex queries themselves
SELECT o.order_id, o.customer_id, SUM(oi.price * oi.quantity) as total
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY o.order_id, o.customer_id;
```

**With abstraction (view):**
```sql
CREATE VIEW recent_order_totals AS
SELECT o.order_id, o.customer_id, SUM(oi.price * oi.quantity) as total
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY o.order_id, o.customer_id;

-- Users interact with simple view
SELECT * FROM recent_order_totals WHERE customer_id = 5;
```

The view **abstracts** the complexity of joins and aggregations.

## Benefits of Encapsulation and Abstraction

1. **Maintainability** - Change internals without affecting users
2. **Safety** - Invalid states become impossible
3. **Simplicity** - Users interact with clear, simple interfaces
4. **Flexibility** - You can optimize or refactor internally
5. **Testing** - You can test components in isolation
6. **Teamwork** - Different teams can work on different abstractions
7. **Reusability** - Well-abstracted components are easier to reuse

## Anti-Patterns: When Encapsulation Goes Wrong

**Over-encapsulation:**
```python
class Person:
    def __init__(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

# This is just hiding things for no reason
p = Person(25)
age = p.get_age()
p.set_age(26)
```

This adds no protection or logic—it's just boilerplate. Use encapsulation when:
- You need to validate values
- You need to perform side effects (logging, triggering updates)
- You want to reserve the right to change implementation

**Leaky abstraction:**
```python
class Database:
    def query(self, sql):
        # The SQL details leak through!
        # Users need to know SQL to use this
        return execute_sql(sql)
```

Better:
```python
class Database:
    def get_users_by_department(self, department):
        # User doesn't need to know SQL
        sql = f"SELECT * FROM users WHERE department = '{department}'"
        return self.query(sql)
```

## Key Takeaways

1. **Encapsulation protects state** - Use private variables and controlled access methods
2. **Abstraction simplifies interfaces** - Hide complexity behind clear methods
3. **Validate at boundaries** - Check inputs to methods, not raw field access
4. **Keep interfaces simple** - Users should understand how to use your code in 30 seconds
5. **Hide implementation details** - Users don't need to know how it works internally
6. **Combine both principles** - Great designs use encapsulation to enforce abstraction
7. **Don't over-engineer** - Simple classes don't need heavy encapsulation
8. **Consistency matters** - If some data is private, make a clear pattern for all of it
