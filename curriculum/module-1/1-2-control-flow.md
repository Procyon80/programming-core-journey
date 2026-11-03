# 📖 Module 1.2: Control Flow - Making Decisions & Loops

## Learning Objectives

By the end of this lesson, you will:
1. Write conditional statements using if, elif, and else
2. Create loops using for and while
3. Understand when to use each type of control structure
4. Write programs that respond to different conditions

---

## 🐍 Python: Making Decisions

### if Statements

An **if** statement executes code only if a condition is true:

```python
age = 20

if age >= 18:
    print("You are an adult")
```

**Output:** `You are an adult`

### if-else Statements

**else** provides alternative code to run if the condition is false:

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**Output:** `You are a minor`

### if-elif-else Statements

Use **elif** (else if) for multiple conditions:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Output:** `Grade: B`

**Important:** Only the first true condition executes. Once an if/elif matches, the rest are skipped.

### Comparison Operators

These return True or False:

```python
x = 10
y = 5

x == y   # False (equal?)
x != y   # True (not equal?)
x > y    # True (greater than?)
x < y    # False (less than?)
x >= y   # True (greater or equal?)
x <= y   # False (less or equal?)
```

### Logical Operators

Combine conditions with **and**, **or**, **not**:

```python
age = 25
has_license = True

# Both must be true
if age >= 18 and has_license:
    print("You can drive")

# Either can be true
if age < 13 or age > 65:
    print("Special pricing applies")

# Negation
if not is_admin:
    print("Permission denied")
```

---

## 🔄 Python: Loops

### for Loops

A **for** loop repeats for each item in a sequence:

```python
# Loop through numbers 0 to 4
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Loop with custom range
for i in range(1, 6):  # 1 to 5 (6 is exclusive)
    print(i * 2)
# Output:
# 2
# 4
# 6
# 8
# 10
```

**range() function:**
- `range(5)` → 0, 1, 2, 3, 4 (0 to n-1)
- `range(2, 7)` → 2, 3, 4, 5, 6 (start to end-1)
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (start, end, step)

### while Loops

A **while** loop repeats as long as a condition is true:

```python
count = 0

while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4
```

**Warning: Infinite loops!**
```python
while True:  # This runs forever!
    print("Help, I'm stuck!")
```

Always make sure the condition eventually becomes false.

### Loop Control: break and continue

**break** exits the loop early:

```python
for i in range(10):
    if i == 5:
        break  # Exit when i is 5
    print(i)
# Output: 0 1 2 3 4
```

**continue** skips to the next iteration:

```python
for i in range(5):
    if i == 2:
        continue  # Skip i=2
    print(i)
# Output: 0 1 3 4
```

---

## 🗄️ SQL: Filtering with Conditions

In SQL, **WHERE** clauses work like Python's **if** statements—they filter rows based on conditions.

### Basic WHERE Conditions

```sql
-- Single condition
SELECT * FROM products WHERE price > 50;

-- Multiple conditions with AND
SELECT * FROM products WHERE price > 50 AND category = 'Electronics';

-- Multiple conditions with OR
SELECT * FROM customers WHERE city = 'New York' OR city = 'Boston';

-- NOT condition
SELECT * FROM products WHERE NOT (category = 'Discontinued');
```

### IN Operator (Like OR for many values)

```sql
-- This:
SELECT * FROM customers WHERE city = 'New York' OR city = 'Boston' OR city = 'Chicago';

-- Is cleaner as:
SELECT * FROM customers WHERE city IN ('New York', 'Boston', 'Chicago');
```

### BETWEEN Operator

```sql
-- Find products priced between $50 and $100
SELECT * FROM products WHERE price BETWEEN 50 AND 100;
```

### NULL Checking

```sql
-- Find customers with no phone number
SELECT * FROM customers WHERE phone IS NULL;

-- Find customers with a phone number
SELECT * FROM customers WHERE phone IS NOT NULL;
```

### Sorting Results: ORDER BY

```sql
-- Sort ascending (default)
SELECT * FROM customers ORDER BY age;

-- Sort descending
SELECT * FROM customers ORDER BY age DESC;

-- Sort by multiple columns
SELECT * FROM customers ORDER BY age ASC, name ASC;
```

---

## 🔢 Exercise 1.3: Temperature Analyzer (Python)

**Problem:**
Write a program that reads daily temperatures for a week and:
1. Finds the highest and lowest temperatures
2. Calculates the average temperature
3. Counts how many days were above freezing (> 0°C)
4. Counts how many days were extremely hot (> 35°C)

**Requirements:**
- Read 7 temperature values from the user
- Display all statistics
- Use only loops and conditionals (no built-in min/max/average for this exercise)

**Example Output:**
```
Enter 7 daily temperatures:
22
18
-2
15
35
38
20

--- Statistics ---
Highest: 38°C
Lowest: -2°C
Average: 20.86°C
Days above freezing: 6
Days extremely hot (>35°C): 2
```

**Hints:**
- Use a loop to read temperatures
- Use variables to track highest, lowest, sum
- Use conditionals to count special cases

---

## 🗄️ Exercise 1.4: Product Analysis (SQL)

**Problem:**
Write SQL queries to answer business questions about products and sales:

**Database Schema:**
```
products table:
- product_id (INTEGER, primary key)
- name (TEXT)
- price (DECIMAL)
- category (TEXT)
- in_stock (BOOLEAN)

orders table:
- order_id (INTEGER, primary key)
- product_id (INTEGER, foreign key)
- quantity (INTEGER)
- order_date (DATE)
```

**Questions (write a query for each):**

1. **List all products in the 'Electronics' category priced between $50-$200, sorted by price ascending**

2. **Find all orders from the last 30 days (assume today is 2025-01-15) that are in stock, sorted by order_date descending**

3. **Count how many products have a price above $100 AND are in stock**

4. **Find all product names that are NOT in the 'Food' category**

5. **List products with IDs 1, 5, 10, or 15 (use IN operator)**

---

## 🧠 Understanding Complexity with Loops

When you see a loop, think about complexity:

```python
# Single loop: O(n)
for i in range(n):
    print(i)

# Nested loops: O(n²)
for i in range(n):
    for j in range(n):
        print(i, j)

# Consecutive loops: O(n) (not multiplied!)
for i in range(n):
    print(i)
for j in range(n):
    print(j)
```

---

## ✅ Lesson Checklist

- [ ] I understand if, elif, and else statements
- [ ] I can write conditional statements with AND/OR
- [ ] I can write for loops with range()
- [ ] I can write while loops
- [ ] I understand break and continue
- [ ] I can analyze loop complexity
- [ ] I can write WHERE clauses in SQL
- [ ] I understand IN, BETWEEN, and NULL operators
- [ ] I can sort SQL results with ORDER BY
- [ ] I have completed Exercise 1.3
- [ ] I have completed Exercise 1.4

---

## 📖 Next Steps

- Move to **Module 1.3: Big O Notation** to formally learn about algorithm analysis
- Or read the deep-dive: `/principles/big-o-notation.md`
