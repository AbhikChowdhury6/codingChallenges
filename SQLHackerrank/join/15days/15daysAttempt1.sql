select distinct s.submission_date, s.numSubs, h.hacker_id, h.name
from Hackers as h
join (select submission_date, hacker_id, count(*) as numSubs
      from Submissions
      group by 1,2
      ) as s
where (s.submission_date, s.numSubs, h.hacker_id) IN (
select s.submission_date, max(s.numSubs), min(h.hacker_id)
from Hackers as h
join (select submission_date, hacker_id, count(*) as numSubs
      from Submissions
      group by 1,2
      ) as s
group by 1
)
order by 1











with dailySubCounts as (
    select sub.submission_date, sub.hacker_id, hac.name, count(*) as numSubs
    from Submissions ass sub
    join Hackers as hac using (hacker_id)
    group by 1,2,3
),


select submission_date, numSubs, hacker_id, name
from dailySubCounts
where (submission_date, numSubs) = 
    (select submission_date, max(numSubs) from dailySubCounts group by submission_date) as mc

