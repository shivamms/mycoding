# Write your MySQL query statement below
SELECT customer_id, COUNT(visit_id) AS count_no_trans FROM
(SELECT v.visit_id, v.customer_id 
FROM Visits v LEFT OUTER JOIN Transactions t 
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL) a
GROUP BY customer_id ORDER BY 2 DESC