# Write your MySQL query statement below
SELECT c1.seat_id
FROM Cinema c1
LEFT OUTER JOIN Cinema c2 ON c2.seat_id = c1.seat_id + 1
LEFT OUTER JOIN Cinema c3 ON c3.seat_id = c1.seat_id - 1
WHERE c1.free = 1 AND (c3.free = 1 OR c2.free = 1)