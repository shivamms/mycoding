# Write your MySQL query statement below
SELECT employee_id,
CASE WHEN MOD(employee_id, 2) > 0 AND NOT (name LIKE 'M%') THEN salary ELSE 0 END bonus
FROM Employees ORDER BY employee_id
