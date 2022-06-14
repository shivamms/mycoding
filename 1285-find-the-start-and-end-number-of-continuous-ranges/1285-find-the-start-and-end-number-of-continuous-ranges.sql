# # Write your MySQL query statement below
# WITH log1 AS 
# (SELECT log_id,  ROW_NUMBER() OVER(ORDER BY log_id ASC) AS rownum FROM logs)
# ,log2 AS 
# (SELECT log_id,  ROW_NUMBER() OVER(ORDER BY log_id ASC) AS rownum FROM logs)
# ,log3 AS 
# (SELECT log_id,  ROW_NUMBER() OVER(ORDER BY log_id ASC) AS rownum FROM logs)
# ,log4 AS 
# (SELECT l1.log_id AS leftid, l2.log_id AS midid, l2.rownum 
# FROM log2 l2 LEFT OUTER JOIN log1 l1 ON l1.rownum = l2.rownum-1)
# ,log5 AS 
# (SELECT leftid, midid, l3.log_id AS rightid
# FROM log4 l4 LEFT OUTER JOIN log3 l3 ON l3.rownum = l4.rownum+1)
# ,log6 AS
# (SELECT CASE WHEN leftid IS NULL OR ABS(leftid-midid) > 1 THEN midid ELSE NULL END AS start_id,
# CASE WHEN rightid is NULL OR ABS(midid-rightid) > 1 THEN midid ELSE NULL END AS end_id
# FROM log5)
# ,log7 AS (SELECT start_id FROM log6 WHERE start_id is NOT NULL)
# ,log8 AS (SELECT end_id FROM log6 WHERE end_id is NOT NULL)
# ,log9 AS (SELECT log7.start_id, log8.end_id FROM log7 JOIN log8 ON 1=1)
# SELECT start_id, MIN(end_id) AS end_id FROM log9 WHERE end_id >= start_id
# GROUP BY start_id

WITH log1 AS
(SELECT log_id, log_id-ROW_NUMBER() OVER(ORDER BY log_id ASC) AS rowgroup FROM Logs)
SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id FROM log1
GROUP BY rowgroup