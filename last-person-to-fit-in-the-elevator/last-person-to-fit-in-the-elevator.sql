# Write your MySQL query statement below
WITH cumulative AS (
    SELECT person_id, person_name, SUM(weight) OVER (ORDER BY turn) AS weight
    FROM Queue)
SELECT person_name FROM cumulative
WHERE weight <= 1000
ORDER BY weight DESC LIMIT 1