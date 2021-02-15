WITH points AS (
    SELECT host_team AS team_id,
        CASE WHEN host_goals > guest_goals THEN 3
             WHEN host_goals = guest_goals THEN 1
             ELSE 0 END num_points 
    FROM matches
    UNION ALL
    SELECT guest_team AS team_id,
        CASE WHEN host_goals < guest_goals THEN 3
             WHEN host_goals = guest_goals THEN 1
             ELSE 0 END num_points 
    FROM matches),
total_points AS (
    SELECT t.team_id, t.team_name, SUM(COALESCE(p.num_points,0)) num_points
    FROM Teams t
    LEFT OUTER JOIN points p ON t.team_id = p.team_id
    GROUP BY t.team_id, t.team_name
)
SELECT team_id, team_name, num_points
FROM total_points
ORDER BY num_points DESC, team_id ASC

