# Write your MySQL query statement below
WITH allstore AS 
(SELECT product_id, 'store1' AS store, store1 AS price
FROM Products WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products WHERE store3 IS NOT NULL)
SELECT product_id, store, price FROM allstore
ORDER BY product_id