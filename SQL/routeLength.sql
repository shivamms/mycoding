--incremental row processing
--compare current row with next row
--self join
-- You've been traveling all over the world for the past year, and now it's time for you to come home. You marked each city that you visited on a map in the order that you visited them, and wrote down the cities' coordinates. For the sake of simplicity, the cities are assigned coordinates on a plane map, so they can be written as (x, y).

-- The information about the cities you visited is stored in the table cities, which has the structure:

-- id: the unique city ID;
-- x: the x coordinate of the city;
-- y: the y coordinate of the city.
-- Now that your journey is over, you're curious about the distance you covered. Given the cities table, your task is to calculate the total length of your route as follows: First, calculate the Euclidean distance between the first and second cities, then add it to the distance between the second and the third cities, and so on.

-- Write a select statement which returns a single total column containing only one row which contains the total length of your route, calculated as described above.

-- Example

-- For the following table cities

-- id	x	y
-- 1	0	0
-- 2	1	1
-- 3	2	2
-- 4	4	2
-- the output should be

-- total
-- 4.828427125
-- Here is how the answer was calculated:
-- distance(0, 0, 1, 1) + distance(1, 1, 2, 2) + distance(2, 2, 4, 2) = sqrt(2) + sqrt(2) + 2 = 4.828427125.

-- The answer should be rounded to exactly 9 digits after the decimal point.

-- [execution time limit] 10 seconds (mysql)
-- MySQL
-- v8.0.22
-- 31245678910
-- /*Please add ; after each select statement*/
-- CREATE PROCEDURE routeLength()
-- BEGIN
--     SELECT
--         ROUND(SUM(DISTANCE(POINT(a.`x`, a.`y`), POINT(b.`x`, b.`y`))), 9) AS `total`
--     FROM 
--         cities AS a
--     JOIN
--         cities AS b ON (b.`id` - a.`id` = 1);
-- END
-- TESTS
-- Tests passed: 4/4.
-- Test 1
-- Test 2
-- Test 3
-- Test 4
-- MORE
-- 14
-- 0


SELECT FORMAT(SUM(SQRT(POWER(c2.x-c1.x,2) + POWER(c2.y-c1.y,2))),9) AS total
FROM cities c1 
JOIN cities c2 WHERE c1.id = c2.id + 1;