# Write your MySQL query statement below
# WITH ordercount AS 
# (SELECT customer_number, COUNT(order_number) oc FROM Orders
# GROUP BY customer_number)
# SELECT customer_number FROM ordercount WHERE oc = (SELECT MAX(oc) FROM ordercount)

# For followup question
SELECT customer_number FROM Orders GROUP BY customer_number ORDER BY COUNT(1) DESC LIMIT 1