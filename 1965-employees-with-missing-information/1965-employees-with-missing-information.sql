# Write your MySQL query statement below
SELECT employee_id FROM
(SELECT e.employee_id, e.name, s.salary 
FROM Employees e LEFT OUTER JOIN Salaries s
ON e.employee_id = s.employee_id
UNION 
SELECT s.employee_id, e.name, s.salary 
FROM Salaries s LEFT OUTER JOIN Employees e
ON s.employee_id = e.employee_id) f
WHERE name IS NULL or salary Is NULL
ORDER BY employee_id
