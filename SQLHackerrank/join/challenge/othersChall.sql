WITH temp AS (
SELECT h.hacker_id, name, COUNT(c.challenge_id) AS total
FROM hackers h 
    JOIN challenges c ON c.hacker_id = h.hacker_id
GROUP BY hacker_id, name
)
SELECT * 
FROM temp
WHERE total = (SELECT MAX(total)
               FROM temp) 
               OR total IN (SELECT total
                FROM temp
                GROUP BY total
                HAVING count(*) = 1
                )
ORDER BY total DESC, hacker_id







with q1 as (
    SELECT 
        h.hacker_id as hackerID,
        h.name as hackerName,
        COUNT(c.challenge_id) as count_challenges
    FROM Hackers h 
    JOIN Challenges c ON h.hacker_id = c.hacker_id
    GROUP BY hackerID, hackerName
),
q2 as (
    SELECT
        MAX(count_challenges) as max_challenges
    FROM q1
),
q3 as (
    SELECT
        count_challenges,
        COUNT(*) as number
    FROM  q1
    WHERE count_challenges NOT IN (SELECT max_challenges FROM q2)
    GROUP BY count_challenges
    HAVING COUNT(*)  = 1
),
q4 AS (
    SELECT DISTINCT
        count_challenges as dist_count_challenges
    FROM q3
)
    SELECT 
        hackerID,
        hackerName,
        count_challenges
    FROM q1
    WHERE count_challenges = (SELECT max_challenges FROM q2)
    OR count_challenges IN (SELECT dist_count_challenges FROM q4)
    ORDER BY count_challenges desc, hackerID asc;





with sub_table as
(
select Id, name, counting
from
(
select h.hacker_id as ID, name, count(challenge_id) as counting
from hackers h join challenges c on h.hacker_id = c.hacker_id
group by h.hacker_id, name
) a
)
select id, name, s.counting
from 
sub_table s
join
(
select counting, count(*) as ranking
from sub_table
group by counting
) b on s.counting =b.counting
where ranking = 1 or s.counting = (select max(counting) from sub_table)
order by counting desc, id asc



SELECT  hacker_id, name, num_challenges FROM
(
    SELECT hacker_id, name, num_challenges,
    COUNT(*) OVER(PARTITION BY num_challenges) AS dupe_count,
    MAX(num_challenges) OVER() AS max_num_challenges
    FROM
    (
        SELECT h.hacker_id, name, COUNT(*) AS num_challenges FROM hackers AS h
        INNER JOIN challenges AS c
        ON h.hacker_id = c.hacker_id``
        GROUP BY h.hacker_id, name
    ) AS T1
) AS T2
WHERE dupe_count = 1 OR num_challenges = max_num_challenges
ORDER BY num_challenges DESC, hacker_id