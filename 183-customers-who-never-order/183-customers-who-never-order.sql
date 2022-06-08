/* Write your T-SQL query statement below */
SELECT c.name AS Customers FROM Customers c 
LEFT OUTER JOIN Orders r ON c.id = r.customerId
WHERE r.customerId IS NULL