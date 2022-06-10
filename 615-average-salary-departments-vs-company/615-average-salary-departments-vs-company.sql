# Write your MySQL query statement below
WITH cmavg AS 
(SELECT DATE_FORMAT(pay_date, '%Y-%m') AS pay_month, AVG(amount) AS avg_amt
 FROM Salary GROUP BY DATE_FORMAT(pay_date, '%Y-%m'))
, dmavg AS 
(SELECT e.department_id, DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month,
AVG(s.amount) AS avg_amt FROM Salary s JOIN Employee e ON s.employee_id = e.employee_id
 GROUP BY e.department_id, DATE_FORMAT(s.pay_date, '%Y-%m'))
 SELECT d.pay_month, d.department_id, 
 CASE WHEN d.avg_amt > c.avg_amt THEN 'higher'
      WHEN d.avg_amt < c.avg_amt THEN 'lower'
      ELSE 'same' END AS comparison
 FROM cmavg c JOIN dmavg d ON c.pay_month = d.pay_month 
 ORDER BY d.department_id, d.pay_month