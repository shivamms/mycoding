# Write your MySQL query statement below
WITH ranked AS (
SELECT  e.Name AS Employee, 
        e.Salary, 
        d.Name AS Department,
        RANK() OVER (PARTITION BY d.Id ORDER BY COALESCE(e.salary,0) DESC) AS                   salaryrank
FROM Department d
JOIN Employee e
ON d.Id = e.DepartmentId)
SELECT Department, Employee, Salary FROM ranked
WHERE salaryrank = 1