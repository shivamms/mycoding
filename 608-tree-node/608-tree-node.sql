# # Write your MySQL query statement below
SELECT id, type FROM
(SELECT id, 'Root' AS type FROM Tree
WHERE p_id IS NULL
UNION ALL
SELECT id, 'Inner' AS type FROM Tree
WHERE p_id IS NOT NULL AND id IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL)
UNION ALL
SELECT id, 'Leaf' AS type FROM Tree
WHERE p_id IS NOT NULL AND id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL)) a
ORDER BY id ASC
