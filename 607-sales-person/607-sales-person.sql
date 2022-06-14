# Write your MySQL query statement below
SELECT s.name  FROM SalesPerson s 
LEFT OUTER JOIN
(SELECT o.sales_id FROM Orders o
JOIN Company c ON o.com_id = c.com_id
WHERE c.name = 'RED') r ON s.sales_id = r.sales_id
WHERE r.sales_id IS NULL