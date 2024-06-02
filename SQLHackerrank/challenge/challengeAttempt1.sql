/*
Enter your query here.
I FORGOT THE HAVING KEYWORD!!!!!
*/


SELECT hacker_id, name, CC FROM

(SELECT hacker_id, name, COUNT(challenge_id) AS CC FROM Hackers
JOIN Challenges USING(hacker_id)
GROUP BY hacker_id, name) AS t3

WHERE CC IN
(SELECT CC FROM
    (SELECT CC, COUNT(CC) AS ChalCountsCounts FROM
        (SELECT hacker_id, name, COUNT(challenge_id) AS CC FROM Hackers
        JOIN Challenges USING(hacker_id)
        GROUP BY hacker_id, name
        ORDER BY COUNT(challenge_id) DESC, hacker_id DESC) AS t1
    GROUP BY CC) AS t2
WHERE ChalCountsCounts = 1)

OR CC = (SELECT MAX(CC) FROM (SELECT hacker_id, name, COUNT(challenge_id) AS CC FROM Hackers
JOIN Challenges USING(hacker_id)
GROUP BY hacker_id, name) AS t4)

ORDER BY CC DESC, hacker_id









