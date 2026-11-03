# 🔄 DRY Principle: Don't Repeat Yourself

## Introduction

**DRY** stands for **"Don't Repeat Yourself"** and is one of the most fundamental principles in programming. It states that:

> *Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.*

When you repeat code, logic, or configuration, you create:
- **Maintenance burden** - Fixing a bug means finding and updating all copies
- **Inconsistency risk** - Updates in one place might miss others
- **Cognitive overhead** - More code to understand and keep in sync
- **Scalability problems** - As systems grow, duplication becomes unmanageable

The DRY principle guides us toward **abstraction, reuse, and automation**.

## The Problem: Violation Examples

### Repeated Code (Copy-Paste)

**Bad - DRY Violation:**
```python
# Customer email validation (1st time)
if "@" not in email or "." not in email:
    print("Invalid email")

# Later in code, validating another email
if "@" not in email or "." not in email:
    print("Invalid email")

# And again elsewhere...
if "@" not in email or "." not in email:
    print("Invalid email")
```

If we need to improve validation (e.g., check domain length), we must change it in **3 places**. We'll inevitably miss one.

**Good - DRY Compliant:**
```python
def is_valid_email(email):
    """Validate email format (single source of truth)."""
    return "@" in email and "." in email

if not is_valid_email(customer_email):
    print("Invalid email")

if not is_valid_email(admin_email):
    print("Invalid email")
```

Now validation is defined once. Update it in one place, and all uses benefit.

### Repeated Logic Patterns

**Bad - DRY Violation:**
```python
# Processing customer data
try:
    customer_name = customer_data['name']
    if not customer_name:
        print("Customer name is required")
        return False
except KeyError:
    print("Customer name is required")
    return False

# Processing product data (same pattern)
try:
    product_name = product_data['name']
    if not product_name:
        print("Product name is required")
        return False
except KeyError:
    print("Product name is required")
    return False
```

**Good - DRY Compliant:**
```python
def get_required_field(data, field_name):
    """Extract and validate required field (reusable)."""
    if field_name not in data:
        raise ValueError(f"{field_name} is required")
    value = data[field_name]
    if not value:
        raise ValueError(f"{field_name} cannot be empty")
    return value

customer_name = get_required_field(customer_data, 'name')
product_name = get_required_field(product_data, 'name')
```

### Configuration Repetition

**Bad - DRY Violation:**
```python
# Database connection (repeated in multiple files)
# file1.py
db_host = "localhost"
db_port = 5432
db_user = "admin"
db_password = "secret123"

# file2.py
db_host = "localhost"
db_port = 5432
db_user = "admin"
db_password = "secret123"

# file3.py
db_host = "localhost"
db_port = 5432
db_user = "admin"
db_password = "secret123"
```

If the password changes, you must update it in 3 places. You'll forget one.

**Good - DRY Compliant:**
```python
# config.py (single source of truth)
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "secret123"
}

# file1.py, file2.py, file3.py
from config import DATABASE_CONFIG
```

Change the config once; all files use the update.

## Solutions: Achieving DRY

### 1. Extract Functions

**Problem:** Same logic appears in multiple places
**Solution:** Create a function and call it

```python
# Bad: Repeated
def process_order_a():
    items = get_items()
    total = sum(item['price'] for item in items)
    tax = total * 0.10
    final = total + tax
    return final

def process_order_b():
    items = get_items()
    total = sum(item['price'] for item in items)
    tax = total * 0.10
    final = total + tax
    return final

# Good: Extracted
def calculate_order_total(items):
    total = sum(item['price'] for item in items)
    tax = total * 0.10
    return total + tax

def process_order_a():
    items = get_items()
    return calculate_order_total(items)

def process_order_b():
    items = get_items()
    return calculate_order_total(items)
```

### 2. Create Classes/Modules

**Problem:** Related functions and data repeated
**Solution:** Group into a class or module

```python
# Bad: Scattered
def validate_user_email(email):
    return "@" in email

def validate_user_age(age):
    return age >= 18

def validate_user_name(name):
    return len(name) > 0

# Good: Organized in class
class User:
    def validate_email(self, email):
        return "@" in email
    
    def validate_age(self, age):
        return age >= 18
    
    def validate_name(self, name):
        return len(name) > 0

user = User()
```

### 3. Use Loops and Collections

**Problem:** Same operation repeated for different data
**Solution:** Loop or map

```python
# Bad: Repeated
print(users[0].name)
print(users[1].name)
print(users[2].name)

# Good: Loop
for user in users:
    print(user.name)
```

### 4. Use Templates/Configuration

**Problem:** Similar structures with variations
**Solution:** Template with parameters

```python
# Bad: Repeated HTML-like structure
page_header = "<header><h1>Home</h1><nav>...</nav></header>"
page_footer = "<footer><p>Copyright 2025</p></footer>"

about_header = "<header><h1>About</h1><nav>...</nav></header>"
about_footer = "<footer><p>Copyright 2025</p></footer>"

# Good: Template
def create_page(title, content):
    header = f"<header><h1>{title}</h1><nav>...</nav></header>"
    body = f"<main>{content}</main>"
    footer = "<footer><p>Copyright 2025</p></footer>"
    return f"{header}\n{body}\n{footer}"

page = create_page("Home", "...")
about = create_page("About", "...")
```

### 5. Use Inheritance/Mixins

**Problem:** Multiple classes need the same methods
**Solution:** Base class or mixin

```python
# Bad: Repeated
class Customer:
    def created_at(self):
        return self.created_date.strftime("%Y-%m-%d")

class Product:
    def created_at(self):
        return self.created_date.strftime("%Y-%m-%d")

# Good: Base class
class Entity:
    def created_at(self):
        return self.created_date.strftime("%Y-%m-%d")

class Customer(Entity):
    pass

class Product(Entity):
    pass
```

## DRY in SQL

**Bad - Repeated query logic:**
```sql
-- Report A
SELECT customer_id, COUNT(*) as order_count
FROM orders
WHERE order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY customer_id;

-- Report B (same filtering)
SELECT customer_id, SUM(total) as total_spent
FROM orders
WHERE order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY customer_id;
```

**Good - Use a VIEW:**
```sql
CREATE VIEW recent_orders AS
SELECT * FROM orders
WHERE order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY);

-- Report A
SELECT customer_id, COUNT(*) as order_count
FROM recent_orders
GROUP BY customer_id;

-- Report B
SELECT customer_id, SUM(total) as total_spent
FROM recent_orders
GROUP BY customer_id;
```

**Or use a CTE:**
```sql
WITH recent_orders AS (
    SELECT * FROM orders
    WHERE order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
)
SELECT customer_id, COUNT(*) as order_count
FROM recent_orders
GROUP BY customer_id;
```

## The Balance: When DRY Goes Too Far

Sometimes premature abstraction creates **unnecessary complexity**. If you only have 2 occurrences and they're in different contexts, copying might be better than forcing an abstraction.

**Guideline:** The "Rule of Three"
- **First occurrence:** Write it normally
- **Second occurrence:** Copy if context is different
- **Third occurrence:** Now extract it

Also consider:
- **Is this likely to change together?** If yes, DRY matters
- **Does the abstraction make code clearer?** If no, reconsider
- **Will extracting create more indirection than clarity?** If yes, maybe keep it simple

## Key Takeaways

1. **DRY reduces bugs** - Changes in one place propagate everywhere
2. **DRY improves readability** - Less code to read and understand
3. **DRY enables scalability** - Systems that grow with minimal code duplication
4. **Extract functions when logic repeats** - Functions are your first tool
5. **Use classes and modules for structure** - Organize related functionality
6. **Templates and configuration fight duplication** - Use them liberally
7. **Don't over-abstract** - Sometimes repetition is honest; wait for the third occurrence
8. **DRY applies to all code** - Tests, SQL, configuration, documentation, all benefit
