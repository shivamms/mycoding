# Write your MySQL query statement below
WITH prod AS
(SELECT sell_date, product FROM Activities
GROUP BY sell_date, product)
SELECT sell_date, COUNT(product) AS num_sold, 
GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM prod GROUP BY sell_date ORDER BY 1,3
