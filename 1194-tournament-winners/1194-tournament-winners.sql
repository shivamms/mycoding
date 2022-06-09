# Write your MySQL query statement below
WITH fc AS
(SELECT p.player_id, p.group_id, first_score AS score FROM Players p
JOIN matches m ON p.player_id = m.first_player
UNION ALL
SELECT p.player_id, p.group_id, second_score AS score FROM Players p
JOIN matches m ON p.player_id = m.second_player)
,ranked AS (SELECT group_id, player_id, 
RANK() OVER(PARTITION BY group_id ORDER BY SUM(score) DESC, player_id ASC) top_rank
FROM fc  GROUP BY group_id, player_id) 
SELECT group_id, player_id FROM ranked WHERE top_rank = 1 ORDER BY group_id, player_id