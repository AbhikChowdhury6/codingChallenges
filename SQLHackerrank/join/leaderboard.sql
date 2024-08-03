select h.hacker_id, h.name, sum(s.score)
from Hackers as h 
join (select hacker_id, challenge_id, max(score) as score
      from Submissions
      group by 1,2
     ) as s using(hacker_id)
group by 1,2
having sum(s.score) > 0
order by sum(s.score) desc, 1