# 📖 Module 1.1: Variables, Types & Basic I/O

## Learning Objectives

By the end of this lesson, you will:
1. Understand Python's basic data types and how to work with them
2. Create variables and assign values correctly
3. Use input/output functions to interact with users
4. Master string formatting for clear output

---

## 🐍 Python: The Building Blocks

### Variables and Assignment

A **variable** is a named container for a value. In Python, you create one simply by assigning a value:

```python
name = "Alice"
age = 25
height = 5.7
is_student = True
```

Python infers the **type** from the value. You don't need to declare types explicitly.

### Basic Data Types

**Integers (int):** Whole numbers
```python
count = 5
year = 2025
temperature = -10
```

**Floats (float):** Decimal numbers
```python
price = 19.99
pi = 3.14159
percentage = 0.85
```

**Strings (str):** Text data
```python
name = "Bob"
message = "Hello, World!"
empty_string = ""
```

**Booleans (bool):** True or False
```python
is_active = True
has_permission = False
```

### Type Conversion

Sometimes you need to convert between types:

```python
age_str = "25"
age = int(age_str)  # Convert string to integer

price = 19.99
price_str = str(price)  # Convert float to string

count = int(3.99)  # Converts to 3 (truncates decimal)

is_valid = bool(1)  # Converts to True (any non-zero is True)
```

### Basic Arithmetic Operations

```python
# Addition
total = 10 + 5  # 15

# Subtraction
difference = 10 - 5  # 5

# Multiplication
product = 3 * 4  # 12

# Division
quotient = 10 / 3  # 3.333...

# Floor division (rounds down)
quotient = 10 // 3  # 3

# Modulo (remainder)
remainder = 10 % 3  # 1

# Exponentiation
power = 2 ** 3  # 8
```

### Input and Output

**Getting user input:**
```python
name = input("What is your name? ")
# User enters: "Charlie"
print(name)  # Output: Charlie
```

The `input()` function always returns a **string**, even if the user enters a number:

```python
age = input("How old are you? ")  # age is a string "25"
age = int(age)  # Convert to integer
```

**Printing output:**
```python
print("Hello, World!")
print(42)
print(3.14)
```

### String Formatting

**Using f-strings (modern and recommended):**
```python
name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.

# Expressions inside braces:
price = 19.99
quantity = 3
total = price * quantity
print(f"Total: ${total:.2f}")  # Output: Total: $59.97
```

**Using .format() (older, still useful):**
```python
print("My name is {} and I am {} years old.".format(name, age))
```

**Simple concatenation:**
```python
print("Hello, " + name + "!")
```

---

## 🗄️ SQL: Retrieving Information

### The SELECT Statement

**SELECT** is the most fundamental SQL operation. It retrieves data from a table.

**Basic syntax:**
```sql
SELECT column1, column2 FROM table_name;
```

**Example:**
```sql
-- Get all columns from the customers table
SELECT * FROM customers;

-- Get specific columns
SELECT name, email FROM customers;

-- Get a single column
SELECT order_id FROM orders;
```

**Result:** A result set (table of data matching your query)

### Filtering with WHERE

Use **WHERE** to filter rows based on conditions:

```sql
-- Find customers with a specific email
SELECT * FROM customers WHERE email = 'alice@example.com';

-- Find orders with a total greater than $100
SELECT * FROM orders WHERE total > 100;

-- Find inactive customers
SELECT * FROM customers WHERE is_active = 0;
```

**Comparison Operators:**
- `=` (equal)
- `<>` or `!=` (not equal)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal)
- `<=` (less than or equal)

**Text matching with LIKE:**
```sql
-- Find names starting with 'A'
SELECT * FROM customers WHERE name LIKE 'A%';

-- Find emails containing 'gmail'
SELECT * FROM customers WHERE email LIKE '%gmail%';
```

**Multiple conditions with AND/OR:**
```sql
-- Customers who are active AND have orders over $50
SELECT * FROM customers WHERE is_active = 1 AND total_spent > 50;

-- Customers in New York OR Los Angeles
SELECT * FROM customers WHERE city = 'New York' OR city = 'Los Angeles';
```

---

## 🔢 Exercise 1.1: Find the Maximum Value (Python)

**Problem:**
Write a Python script that takes a list of numbers and finds the maximum value **without using the built-in `max()` function**.

**Requirements:**
- Read 5 numbers from user input
- Store them in a list
- Find and print the maximum value
- Print the index (position) of the maximum value

**Example Output:**
```
Enter 5 numbers:
10
5
23
15
8
The maximum value is: 23
It is at index: 2
```

**Hints:**
- Use a loop to read the numbers
- Compare each number to track the maximum

**Expected Complexity:** O(n) - linear

---

## 🗄️ Exercise 1.2: Customer Query (SQL)

**Problem:**
Write a SQL query that retrieves all customers who have placed an order with a total amount greater than $50, sorted by total amount in descending order.

**Database Schema:**
```
customers table:
- customer_id (INTEGER, primary key)
- name (TEXT)
- email (TEXT)

orders table:
- order_id (INTEGER, primary key)
- customer_id (INTEGER, foreign key)
- total (DECIMAL)
- order_date (DATE)
```

**Requirements:**
- Select customers with orders over $50
- Include customer name, email, order ID, and order total
- Sort by order total from highest to lowest
- Remove duplicates if a customer has multiple qualifying orders

**Expected Output:**
```
| name    | email              | order_id | total |
|---------|-------------------|----------|-------|
| Alice   | alice@example.com  | 102      | 150.00|
| Bob     | bob@example.com    | 103      | 99.99 |
| Charlie | charlie@example.com| 101      | 75.50 |
```

---

## 📚 Connecting the Dots

Both Python and SQL are about **working with data**:
- **Python** helps you manipulate data with variables, types, and logic
- **SQL** helps you retrieve and filter data from databases

A typical workflow:
1. Query data from the database using SQL
2. Process it in Python
3. Display results to the user

---

## ✅ Lesson Checklist

- [ ] I can create variables and assign different data types
- [ ] I can perform basic arithmetic operations
- [ ] I can convert between data types
- [ ] I can use input() to get user data
- [ ] I can format strings using f-strings
- [ ] I understand SELECT and WHERE in SQL
- [ ] I can filter data with AND/OR conditions
- [ ] I have completed Exercise 1.1
- [ ] I have completed Exercise 1.2

---

## 📖 Next Steps

- Move to **Module 1.2: Control Flow** to learn about loops and conditional logic
- Or jump to the exercises directory to start working: `/python/module-1/exercises/`
