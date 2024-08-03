select h.hacker_id, h.name from
Hackers as h
join Submissions as s using(hacker_id)
join Challenges as c using(challenge_id)
join Difficulty as d using(difficulty_level)
where s.score = d.score
group by h.hacker_id, h.name
having count(c.challenge_id) > 1
order by count(c.challenge_id)  desc, h.hacker_id