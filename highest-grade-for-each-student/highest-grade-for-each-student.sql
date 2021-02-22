# Write your MySQL query statement below
WITH ranked AS (
    SELECT student_id, course_id,grade,
        RANK() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC) graderank
    FROM Enrollments)
SELECT student_id, course_id,grade 
FROM ranked
WHERE graderank = 1
ORDER BY student_id
