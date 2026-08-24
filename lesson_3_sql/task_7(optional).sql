WITH order_stats AS (
    SELECT customer_id,
           COUNT(*) AS total_orders,
           SUM(amount) AS total_amount
    FROM Orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 2
),
delivered_customers AS (
    SELECT DISTINCT customer
    FROM Shippings
    WHERE status = 'Delivered'
)
SELECT c.first_name || ' ' || c.last_name AS full_name,
       c.country,
       os.total_orders,
       os.total_amount
FROM Customers c
JOIN order_stats os ON c.customer_id = os.customer_id
JOIN delivered_customers dc ON c.customer_id = dc.customer
ORDER BY full_name;