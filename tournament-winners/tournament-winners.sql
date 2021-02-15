# Write your MySQL query statement below
WITH scores AS (
    SELECT first_player AS player_id, SUM(first_score) score
    FROM Matches
    GROUP BY first_player
    UNION ALL
    SELECT second_player AS player_id, SUM(second_score) score
    FROM Matches
    GROUP BY second_player),
total_score AS (
    SELECT p.group_id, p.player_id, SUM(COALESCE(s.score,0)) total_score
    FROM Players p 
    LEFT OUTER JOIN scores s ON p.player_id = s.player_id
    GROUP BY p.group_id,p.player_id),
max_score AS (
    SELECT group_id, MAX(total_score) max_score
    FROM total_score
    GROUP BY group_id)
SELECT m.group_id, MIN(player_id) player_id
FROM max_score m 
JOIN total_score t ON m.group_id = t.group_id AND m.max_score = t.total_score
GROUP BY m.group_id 
ORDER BY m.group_id

    