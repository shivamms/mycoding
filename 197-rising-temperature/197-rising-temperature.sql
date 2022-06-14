# Write your MySQL query statement below
# WITH cte AS 
# (SELECT id, recordDate, temperature, ROW_NUMBER() OVER(ORDER BY recordDate) AS rn FROM Weather)
# SELECT w2.id AS id
# FROM cte w1 JOIN cte w2 ON w2.rn = w1.rn + 1
# WHERE CASE WHEN DATEDIFF(w2.recordDate, w1.recordDate) = 1 
# AND w2.temperature > w1.temperature THEN w2.id END IS NOT NULL
# ORDER BY w1.recordDate

SELECT w2.id
FROM Weather w1 JOIN Weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
WHERE w2.temperature > w1.temperature