# Write your MySQL query statement below
SELECT firstname, lastname, city, state FROM Person p
LEFT OUTER JOIN Address a ON p.personId = a.personId