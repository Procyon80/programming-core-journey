-- Exercise 1.1: Customer Orders Query - Solution

SELECT
    c.name,
    c.email,
    o.order_id,
    o.order_date,
    o.total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total > 50
ORDER BY o.total DESC;

-- Explanation:
-- 1. SELECT: Choose customer name and email, plus order details
-- 2. FROM: Start with customers table (aliased as 'c')
-- 3. INNER JOIN: Connect to orders table on matching customer_id
--    - INNER JOIN only returns rows with matching customers in both tables
-- 4. WHERE: Filter to show only orders with total > $50
-- 5. ORDER BY: Sort by order total descending (highest first)

-- Bonus: Add row numbers to show ranking
SELECT
    ROW_NUMBER() OVER (ORDER BY o.total DESC) as rank,
    c.name,
    c.email,
    o.order_id,
    o.order_date,
    o.total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total > 50
ORDER BY o.total DESC;

-- Bonus: Count orders per customer
SELECT
    c.name,
    c.email,
    COUNT(o.order_id) as order_count,
    SUM(o.total) as total_spent,
    o.total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total > 50
GROUP BY c.customer_id, c.name, c.email, o.total
ORDER BY total_spent DESC;

-- Bonus: Filter by 2025 orders only
SELECT
    c.name,
    c.email,
    o.order_id,
    o.order_date,
    o.total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total > 50 AND YEAR(o.order_date) = 2025
ORDER BY o.total DESC;

-- Complexity Analysis:
-- Time: O(n log n) typically - depends on indexing and database optimizer
-- Space: O(n) - results set size is proportional to matching orders
