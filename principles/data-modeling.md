# 🗂️ Data Modeling: Structuring Information Effectively

## Introduction

Data modeling is the process of designing **how data is organized, stored, and related** in a database. Good data modeling ensures that your data is:
- **Consistent** - No contradictory information
- **Efficient** - Minimal storage and fast queries
- **Maintainable** - Easy to update and understand
- **Scalable** - Can grow without structural problems

Poor data modeling leads to duplicate data, inconsistencies, performance problems, and headaches when you need to change things. In this principle, we learn to think like a database architect.

## Core Concepts

### Entities and Attributes

An **entity** is a "thing" in your system (a person, an order, a product). An **attribute** is a property of that entity.

**Example: An e-commerce system**
- **Entity: Customer**
  - Attributes: customer_id, name, email, phone, address
- **Entity: Product**
  - Attributes: product_id, name, price, category, stock_quantity
- **Entity: Order**
  - Attributes: order_id, customer_id, order_date, total_amount

### Relationships

Entities relate to each other:
- **One-to-One (1:1):** A customer has one primary address
- **One-to-Many (1:N):** A customer has many orders
- **Many-to-Many (N:N):** An order contains many products, and a product appears in many orders

### Keys

A **key** uniquely identifies a record:
- **Primary Key (PK):** Uniquely identifies a row in a table (e.g., customer_id)
- **Foreign Key (FK):** Refers to a primary key in another table (e.g., an order's customer_id)

**Example:**
```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

Here, `customer_id` in the orders table is a **foreign key** linking to the customers table.

## Normalization: Eliminating Redundancy

Normalization is a process of organizing a database to **minimize data duplication and dependency**. It has progressive levels, each stricter than the last.

### First Normal Form (1NF)

**Rule:** Every field must contain **atomic (indivisible) values**, and there should be **no repeating groups**.

**Bad (violates 1NF):**
```
| student_id | name    | courses               |
|---|---|---|
| 1 | Alice | Math, Physics, Biology |
| 2 | Bob   | Chemistry               |
```

The `courses` column contains multiple values in a single field.

**Good (1NF compliant):**
```
| student_id | name  | course      |
|---|---|---|
| 1 | Alice | Math        |
| 1 | Alice | Physics     |
| 1 | Alice | Biology     |
| 2 | Bob   | Chemistry   |
```

Each row contains a single, atomic value for the course.

### Second Normal Form (2NF)

**Rule:** Must be in 1NF, AND **non-primary-key attributes must depend on the entire primary key** (not just part of it).

This only matters if your primary key is **composite** (made of multiple columns).

**Bad (violates 2NF):**
```
| student_id | course | instructor | instructor_office |
|---|---|---|---|
| 1 | Math | Dr. Smith | Building A, Room 101 |
| 2 | Math | Dr. Smith | Building A, Room 101 |
```

The `instructor_office` depends on `instructor`, not on the full primary key (student_id, course).

**Good (2NF compliant):**

*Table 1: Enrollment*
```
| student_id | course |
|---|---|
| 1 | Math   |
| 2 | Math   |
```

*Table 2: Course Instructors*
```
| course | instructor | instructor_office |
|---|---|---|
| Math   | Dr. Smith  | Building A, Room 101 |
```

Now each attribute depends on the full context.

### Third Normal Form (3NF)

**Rule:** Must be in 2NF, AND **non-primary-key attributes must not depend on other non-primary-key attributes**.

In other words, eliminate **transitive dependencies**.

**Bad (violates 3NF):**
```
| student_id | name  | major | major_advisor      |
|---|---|---|---|
| 1 | Alice | CS    | Dr. Johnson |
| 2 | Bob   | CS    | Dr. Johnson |
| 3 | Carol | Math  | Dr. Lee     |
```

The `major_advisor` depends on `major`, not on the primary key `student_id`. If Dr. Johnson changes departments, we'd have to update multiple rows.

**Good (3NF compliant):**

*Table 1: Students*
```
| student_id | name  | major |
|---|---|---|
| 1 | Alice | CS    |
| 2 | Bob   | CS    |
| 3 | Carol | Math  |
```

*Table 2: Majors*
```
| major | major_advisor |
|---|---|
| CS    | Dr. Johnson   |
| Math  | Dr. Lee       |
```

Now each table is independent, and updates affect only one place.

## Practical Normalization Example

### Starting Point: Unnormalized Sales Data
```
| order_id | customer_name | product1      | product1_price | product2      | product2_price |
|---|---|---|---|---|---|
| 101 | Alice | Laptop        | 1000           | Mouse         | 25             |
| 102 | Bob   | Keyboard      | 75             | NULL          | NULL           |
```

**Problems:**
- Repeating product columns (no scalability)
- Data redundancy (customer_name in every row)
- Difficult to query

### Normalized to 3NF
```
Customers:
| customer_id | name  |
|---|---|
| 1 | Alice |
| 2 | Bob   |

Orders:
| order_id | customer_id | order_date |
|---|---|---|
| 101 | 1 | 2025-01-15 |
| 102 | 2 | 2025-01-16 |

Order_Items:
| item_id | order_id | product_id | quantity | price |
|---|---|---|---|---|
| 1 | 101 | 1 | 1 | 1000 |
| 2 | 101 | 2 | 1 | 25 |
| 3 | 102 | 3 | 1 | 75 |

Products:
| product_id | name     | standard_price |
|---|---|---|
| 1 | Laptop   | 1000       |
| 2 | Mouse    | 25         |
| 3 | Keyboard | 75         |
```

**Advantages:**
- No repeating columns
- Customer name stored once
- Easy to add new products to an order
- Efficient updates (if a product's price changes, update once)

## Denormalization: When to Break the Rules

Sometimes we **intentionally denormalize** for performance. If you have a report that always needs customer name with orders, you might store it in the Orders table too, accepting the redundancy for query speed.

**When to denormalize:**
- You have a very heavy read load and need speed
- You've measured and confirmed it's a bottleneck
- You accept the maintenance burden

**Never denormalize without a good reason.**

## Real-World Patterns

### One-to-One Relationship
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name TEXT,
    office_id INT UNIQUE,  -- Each employee has one office
    FOREIGN KEY (office_id) REFERENCES offices(office_id)
);
```

### One-to-Many Relationship
```sql
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    name TEXT
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title TEXT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
```

### Many-to-Many Relationship
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name TEXT
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    title TEXT
);

CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

The `enrollments` table is a **junction table** that connects students and courses.

## Key Takeaways

1. **Normalize to 3NF by default** - It eliminates most redundancy issues
2. **Think about relationships first** - One-to-many and many-to-many shape your structure
3. **Use foreign keys** - They maintain data integrity and document relationships
4. **Update in one place** - Good modeling means changes affect only the right spot
5. **Denormalization is a performance tool, not a design tool** - Use it sparingly and deliberately
6. **A good data model is worth the upfront effort** - It saves you headaches later
