# 🎯 Separation of Concerns: Keeping Responsibilities Distinct

## Introduction

**Separation of Concerns (SoC)** is the principle that a system should be divided into parts that each address a **single, well-defined concern**. Each component should have one reason to change.

This principle helps because:
- **Independent evolution** - You can improve one part without affecting others
- **Easier testing** - Test each concern separately
- **Better organization** - Code that does one thing is easier to find and understand
- **Reusability** - A component focused on one job can be reused in different contexts
- **Reduced coupling** - Changes in one area don't ripple through the system

Think of it like a restaurant: The kitchen (food preparation) is separate from the waitstaff (customer interaction). If you improve the menu, the waitstaff's job doesn't change.

## Anti-Pattern: God Class (Violates SoC)

**Bad Example:**
```python
class UserManager:
    """Violates SoC: Does everything related to users"""
    
    def create_user(self, name, email, password):
        """Concern 1: User creation"""
        # Validate email format
        if "@" not in email:
            raise ValueError("Invalid email")
        
        # Hash password (cryptography concern)
        import hashlib
        hashed = hashlib.sha256(password.encode()).hexdigest()
        
        # Save to database (database concern)
        self.db.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            (name, email, hashed)
        )
        
        # Send welcome email (email concern)
        self.smtp.send_mail(email, "Welcome!", "Thanks for signing up")
        
        # Log the action (logging concern)
        print(f"User created: {name}")
        
        return True
```

**Problems:**
- Creating a user touches 6 different concerns (validation, cryptography, database, email, logging, business logic)
- To test user creation, you need a real database, email service, etc.
- To change how emails are sent, you must modify the user manager
- This class has 6 reasons to change, not 1

## Solution: Separation of Concerns

Divide into focused components:

```python
# Concern 1: Email validation
class EmailValidator:
    @staticmethod
    def is_valid(email):
        return "@" in email and "." in email

# Concern 2: Password handling
class PasswordManager:
    @staticmethod
    def hash_password(password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password, hashed):
        return PasswordManager.hash_password(password) == hashed

# Concern 3: Email notification
class EmailService:
    def __init__(self, smtp_connection):
        self.smtp = smtp_connection
    
    def send_welcome_email(self, email):
        self.smtp.send_mail(email, "Welcome!", "Thanks for signing up")

# Concern 4: Data persistence
class UserRepository:
    def __init__(self, database):
        self.db = database
    
    def save(self, user_data):
        self.db.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (user_data['name'], user_data['email'], user_data['password'])
        )

# Concern 5: Logging
class Logger:
    @staticmethod
    def log(message):
        print(f"[LOG] {message}")

# Concern 6: Business logic (orchestration)
class UserService:
    """Orchestrates user creation by delegating to focused components"""
    
    def __init__(self, repository, email_service, logger):
        self.repository = repository
        self.email_service = email_service
        self.logger = logger
    
    def create_user(self, name, email, password):
        # Validate
        if not EmailValidator.is_valid(email):
            raise ValueError("Invalid email format")
        
        # Hash password
        hashed_password = PasswordManager.hash_password(password)
        
        # Save to database
        user_data = {
            'name': name,
            'email': email,
            'password': hashed_password
        }
        self.repository.save(user_data)
        
        # Send email
        self.email_service.send_welcome_email(email)
        
        # Log
        self.logger.log(f"User created: {name}")
        
        return True

# Usage
user_service = UserService(
    repository=UserRepository(database),
    email_service=EmailService(smtp),
    logger=Logger()
)
user_service.create_user("Alice", "alice@example.com", "secret123")
```

**Benefits:**
- Each class has one responsibility and one reason to change
- Test `EmailValidator` without touching the database
- Test `UserRepository` without sending emails
- Swap implementations easily (e.g., different email providers)
- New concerns can be added without modifying existing code

## Separation of Concerns: Layered Architecture

A common way to apply SoC is to organize code into **layers**, each with a specific responsibility:

```
┌─────────────────────────────────────┐
│   Presentation Layer                │  (UI, REST endpoints, views)
│   - Handle HTTP requests            │
│   - Format responses                │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   Business Logic Layer              │  (Use cases, services, rules)
│   - Implement business rules        │
│   - Orchestrate operations          │
│   - Validate business constraints   │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   Data Access Layer                 │  (Database, queries, repos)
│   - Perform database operations     │
│   - Handle persistence              │
│   - Query data                      │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   External Services Layer           │  (APIs, email, payments)
│   - Call external systems           │
│   - Handle third-party integrations │
└─────────────────────────────────────┘
```

### Example: Layered E-Commerce Order System

**Presentation Layer:**
```python
from flask import Flask, request, jsonify
from business_logic import OrderService

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def create_order():
    # Concern: Handle HTTP request
    data = request.json
    
    # Delegate to business layer
    service = OrderService()
    order = service.create_order(
        user_id=data['user_id'],
        items=data['items']
    )
    
    # Concern: Format response
    return jsonify({'order_id': order.id, 'status': order.status})
```

**Business Logic Layer:**
```python
class OrderService:
    def create_order(self, user_id, items):
        # Concern: Implement business rules
        if not items:
            raise ValueError("Order must contain items")
        
        # Validate user has funds
        user = self.user_repo.get(user_id)
        total = sum(item['price'] for item in items)
        if user.balance < total:
            raise ValueError("Insufficient funds")
        
        # Create order
        order = Order(user_id=user_id, items=items)
        
        # Charge payment
        payment_service = PaymentService()
        payment_service.charge(user_id, total)
        
        # Persist order
        self.order_repo.save(order)
        
        return order
```

**Data Access Layer:**
```python
class OrderRepository:
    def __init__(self, database):
        self.db = database
    
    def save(self, order):
        # Concern: Persist to database
        self.db.execute(
            "INSERT INTO orders (user_id, total, created_at) VALUES (?, ?, ?)",
            (order.user_id, order.total, datetime.now())
        )
        
        for item in order.items:
            self.db.execute(
                "INSERT INTO order_items (order_id, item_id, quantity) VALUES (?, ?, ?)",
                (order.id, item['id'], item['quantity'])
            )
```

**External Services Layer:**
```python
class PaymentService:
    def charge(self, user_id, amount):
        # Concern: Interact with payment gateway
        gateway = StripeGateway()
        gateway.charge(user_id, amount)
        
        # Log transaction
        Logger.log(f"Charged user {user_id}: ${amount}")
```

### Benefits of Layered Architecture

- **Presentation changes don't affect business logic** - Swap REST API for GraphQL
- **Business rules are testable** - Test without HTTP or database
- **Database changes are isolated** - Switch from SQL to NoSQL
- **External services are swappable** - Test with mock payment service
- **Teams can work independently** - Frontend, backend, DevOps teams separate

## Separation of Concerns: Data and Logic

Keep **data structures** separate from **operations** on them:

**Bad: Mixed concerns**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def save_to_database(self):
        # Product shouldn't know about databases
        db.execute("INSERT INTO products VALUES (?, ?)", (self.name, self.price))
    
    def send_to_warehouse_system(self):
        # Product shouldn't know about warehouse systems
        warehouse_api.post("/inventory", {'name': self.name, 'price': self.price})

# Usage
product = Product("Laptop", 999)
product.save_to_database()
product.send_to_warehouse_system()
```

**Good: Separated concerns**
```python
class Product:
    """Data only: represents a product"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductRepository:
    """Data access: persists products"""
    def save(self, product):
        db.execute("INSERT INTO products VALUES (?, ?)", (product.name, product.price))

class WarehouseIntegration:
    """External integration: communicates with warehouse"""
    def send_product(self, product):
        warehouse_api.post("/inventory", {'name': product.name, 'price': product.price})

# Usage
product = Product("Laptop", 999)
ProductRepository().save(product)
WarehouseIntegration().send_product(product)
```

The Product class now has **one concern**: being a data container. Changes to persistence or warehouse integration don't affect it.

## SoC in SQL

Apply SoC by organizing database components:

**Concerns to separate:**

1. **Schema (structure)** - What tables and columns exist
2. **Views (abstractions)** - Simplified interfaces for queries
3. **Stored procedures (logic)** - Business rules in the database
4. **Permissions (security)** - Who can access what

```sql
-- Concern 1: Raw tables (schema)
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    total DECIMAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Concern 2: Business abstraction (view)
CREATE VIEW customer_order_summary AS
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) as order_count,
    SUM(o.total) as lifetime_value
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

-- Concern 3: Business logic (stored procedure)
CREATE PROCEDURE add_order(
    IN p_customer_id INT,
    IN p_total DECIMAL
)
BEGIN
    INSERT INTO orders (customer_id, total) VALUES (p_customer_id, p_total);
    UPDATE customers SET loyalty_points = loyalty_points + 10 WHERE customer_id = p_customer_id;
END;

-- Concern 4: Security (permissions)
GRANT SELECT ON customer_order_summary TO analyst_role;
GRANT EXECUTE ON add_order TO admin_role;
GRANT SELECT ON orders TO readonly_user;
```

Users interact with views and procedures, not raw tables. Changes to table structure don't break their code.

## Key Takeaways

1. **One responsibility per component** - Each class/module should have one reason to change
2. **Organize into layers** - Presentation, business logic, data access, external services
3. **Isolate concerns** - Changes in one layer shouldn't ripple through others
4. **Use abstractions** - Views, services, repositories hide implementation
5. **Test each concern independently** - Mock out other layers
6. **Build for change** - Teams should be able to work on different layers in parallel
7. **Avoid god objects** - A class doing too much is a sign to refactor
8. **SoC improves reusability** - A focused component can be used in different contexts
9. **Communicate across layer boundaries** - Use interfaces and contracts
10. **Balance abstraction and practicality** - Don't over-engineer, but don't mix concerns either
