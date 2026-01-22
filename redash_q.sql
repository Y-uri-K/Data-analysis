--total points by levels
SELECT
    l.level_id,
    l.difficulty,
    SUM(ge.points) AS total_points
FROM game_events ge
JOIN levels l ON ge.level_id = l.level_id
GROUP BY l.level_id, l.difficulty
ORDER BY total_points DESC;

--total players by date
SELECT
    DATE(registration_date) AS day,
    COUNT(*) AS new_players,
    SUM(COUNT(*)) OVER (ORDER BY DATE(registration_date)) AS cumulative_players
FROM players
GROUP BY DATE(registration_date)
ORDER BY day;

--Activity by day
SELECT
    DATE(event_time) AS day,
    COUNT(*) AS events_count
FROM game_events
GROUP BY day
ORDER BY day;
