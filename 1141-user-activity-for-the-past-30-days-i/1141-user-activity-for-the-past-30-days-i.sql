# Write your MySQL query statement below
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity 
WHERE activity_date BETWEEN CONVERT('2019-06-28', DATE) AND CONVERT('2019-07-27', DATE)
GROUP BY activity_date ORDER BY activity_date