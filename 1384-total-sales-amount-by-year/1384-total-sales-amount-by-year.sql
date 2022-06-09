# # Write your MySQL query statement below
# WITH RECURSIVE yearly_sales AS
# (SELECT product_id, YEAR(period_start) AS start_year, YEAR(period_end) AS end_year,
#     YEAR(period_end) - YEAR(period_start) + 1 AS years, YEAR(period_start) AS single_year 
#  FROM Sales
# UNION ALL
#  SELECT product_id, start_year, end_year, years, single_year + 1 
#  FROM yearly_sales
#  WHERE single_year < end_year)
# ,sales_with_all_dates AS 
# (SELECT product_id, single_year, CONVERT(CONCAT(CONVERT(single_year,CHAR), '-01-01'),DATE)           single_year_start_date,
#     CONVERT(CONCAT(CONVERT(single_year,CHAR), '-12-31'),DATE) single_year_end_date
#  FROM yearly_sales)
# ,sales_with_period_dates AS
# (SELECT d.product_id, d.single_year,
#     CASE WHEN s.period_start > d.single_year_start_date THEN s.period_start ELSE                        d.single_year_start_date END AS year_start_date,
#     CASE WHEN s.period_end < d.single_year_end_date THEN s.period_end ELSE d.single_year_end_date        END AS year_end_date, 
#     s.average_daily_sales
#  FROM sales_with_all_dates d
# JOIN Sales s ON d.product_id = s.product_id)
# SELECT s.product_id, p.product_name, CONVERT(s.single_year,CHAR) AS report_year, 
# (DATEDIFF(s.year_end_date,s.year_start_date)+1) * s.average_daily_sales AS total_amount 
# FROM sales_with_period_dates s JOIN Product p ON s.product_id = p.product_id
# ORDER BY s.product_id, s.single_year
WITH RECURSIVE dates AS 
(SELECT min(period_start) AS d FROM Sales
UNION ALL
SELECT DATE_ADD(d, interval 1 day) as d FROM dates 
WHERE d <= (SELECT max(period_end) FROM Sales))
SELECT s.product_id, p.product_name,
CONVERT(YEAR(d.d), CHAR) AS report_year, 
SUM(s.average_daily_sales) AS total_amount
FROM Sales s JOIN dates d ON d.d BETWEEN s.period_start AND s.period_end
JOIN Product p ON s.product_id = p.product_id
GROUP BY 1, 2, 3
ORDER BY 1,2


