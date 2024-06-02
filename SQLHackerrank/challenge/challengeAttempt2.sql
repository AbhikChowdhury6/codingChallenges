/*
Enter your query here.
*/
WITH hackerCounts AS (
    SELECT hacker_id, name, COUNT(challenge_id) AS CC FROM Hackers
    JOIN Challenges USING(hacker_id)
    GROUP BY hacker_id, name),
    
chalCounts AS (
    SELECT CC, COUNT(CC) AS ChalCountsCounts FROM hackerCounts
    GROUP BY CC
    HAVING ChalCountsCounts = 1 OR CC = (SELECT MAX(CC) FROM hackerCounts))

SELECT hacker_id, name, CC FROM hackerCounts
where CC IN (SELECT CC FROM chalCounts)
ORDER BY CC DESC, hacker_id