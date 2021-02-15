SELECT * FROM (
SELECT teams.team_id, teams.team_name, 
CASE WHEN SUM(combined.num_points) IS NULL THEN 0
ELSE SUM(combined.num_points) END num_points
FROM
(SELECT h.team_id, 
CASE WHEN m.host_goals > m.guest_goals THEN 3
     WHEN m.host_goals = m.guest_goals THEN 1
     ELSE 0 END num_points 
FROM Teams h, Matches m
WHERE h.team_id = m.host_team
UNION ALL
SELECT g.team_id, 
CASE WHEN m.guest_goals > m.host_goals THEN 3
     WHEN m.guest_goals = m.host_goals THEN 1
     ELSE 0 END num_points 
FROM Teams g, Matches m
WHERE g.team_id = m.guest_team) combined
RIGHT OUTER JOIN Teams teams ON teams.team_id = combined.team_id
GROUP BY teams.team_id, teams.team_name) result
ORDER BY num_points DESC, team_id ASC

