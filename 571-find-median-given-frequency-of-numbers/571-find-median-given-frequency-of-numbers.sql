# Write your MySQL query statement below
WITH RECURSIVE expanded AS
(SELECT num, frequency, 1 AS n FROM Numbers
UNION ALL
SELECT num, frequency, n + 1 FROM expanded WHERE n < frequency)
, expanded_with_rownum AS (SELECT num, frequency, ROW_NUMBER() OVER(ORDER BY num, n) AS rownum FROM expanded)
, expanded_with_mid AS (SELECT MAX(rownum) AS max_rownum,
CASE WHEN MOD(MAX(rownum), 2) = 0 THEN (MAX(rownum)/2) ELSE CEILING(MAX(rownum)/2) END AS mid1,
CASE WHEN MOD(MAX(rownum), 2) = 0 THEN (MAX(rownum)/2)+1 ELSE CEILING(MAX(rownum)/2) END AS mid2
FROM expanded_with_rownum)
SELECT ROUND(AVG(num),1) AS median FROM expanded_with_rownum 
JOIN expanded_with_mid ON 1 = 1 AND rownum IN (mid1, mid2)