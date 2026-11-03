# Exercise 1.1: Customer Orders Query

## Problem Statement

Write a SQL query that retrieves customers who have placed orders with a total amount greater than $50, including their details and order information, sorted by order total from highest to lowest.

## Database Schema

```sql
customers table:
- customer_id (INTEGER, primary key)
- name (TEXT)
- email (TEXT)
- city (TEXT)

orders table:
- order_id (INTEGER, primary key)
- customer_id (INTEGER, foreign key)
- order_date (DATE)
- total (DECIMAL)
```

## Requirements

1. Select customers with orders over $50
2. Include columns: customer name, email, order_id, order_date, total
3. Sort by order total from highest to lowest
4. If customer has multiple qualifying orders, show all of them
5. Use meaningful column aliases for clarity

## Expected Output Format

```
| name    | email              | order_id | order_date | total  |
|---------|-------------------|----------|------------|--------|
| Alice   | alice@example.com  | 102      | 2025-01-15 | 150.00 |
| Bob     | bob@example.com    | 103      | 2025-01-14 | 99.99  |
| Charlie | charlie@example.com| 101      | 2025-01-13 | 75.50  |
```

## Bonus Challenges

1. **Add row numbers:** Add a column showing the rank of orders by total (highest = 1)
2. **Add aggregate:** Show the count of orders per customer
3. **Performance:** Add a WHERE clause to only show orders from 2025

## Complexity Note

With proper indexing on customer_id and order_id, this query is typically O(n log n) or O(n) depending on the database optimizer.

## Testing

Create test data:
```sql
INSERT INTO customers VALUES (1, 'Alice', 'alice@example.com', 'NYC');
INSERT INTO customers VALUES (2, 'Bob', 'bob@example.com', 'LA');
INSERT INTO customers VALUES (3, 'Charlie', 'charlie@example.com', 'Chicago');

INSERT INTO orders VALUES (101, 3, '2025-01-13', 75.50);
INSERT INTO orders VALUES (102, 1, '2025-01-15', 150.00);
INSERT INTO orders VALUES (103, 2, '2025-01-14', 99.99);
INSERT INTO orders VALUES (104, 1, '2025-01-10', 45.00);  -- Less than 50, exclude
```
