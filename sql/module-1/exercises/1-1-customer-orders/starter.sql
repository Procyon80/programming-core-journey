-- Exercise 1.1: Customer Orders Query - Starter
-- TODO: Write a query to find customers with orders over $50

-- Start with this basic structure and build from there:
-- SELECT [columns]
-- FROM [table]
-- WHERE [condition]
-- ORDER BY [column]

SELECT
    -- TODO: Add customer name, email
    -- TODO: Add order details (order_id, order_date, total)
FROM customers
-- TODO: Join with orders table
WHERE
    -- TODO: Filter for orders with total > 50
ORDER BY
    -- TODO: Sort by total descending
