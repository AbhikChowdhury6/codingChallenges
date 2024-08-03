/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
/*
Enter your query here.
*/

with dailySubCounts as (
    select sub.submission_date, sub.hacker_id, hac.name, count(*) as numSubs
    from Submissions as sub
    join Hackers as hac on sub.hacker_id = hac.hacker_id
    group by sub.submission_date, sub.hacker_id, hac.name
),

dailyMaxSubCount as (
    select submission_date, max(numSubs) as maxSubs
    from dailySubCounts
    group by submission_date
),

minHidMaxSubCount as (
    select dm.submission_date, min(sc.hacker_id) as minHid
    from dailySubCounts as sc
    join dailyMaxSubCount as dm on sc.submission_date = dm.submission_date and sc.numSubs = dm.maxSubs
    group by dm.submission_date
),

dailyMaxHackers as (
    select mHidD.submission_date, dsc.hacker_id, dsc.name
    from minHidMaxSubCount as mHidD
    join dailySubCounts as dsc on mHidD.submission_date = dsc.submission_date and mHidD.minHid = dsc.hacker_id
),

dailyNumHackers as (
    select submission_date, count(*) as unqHackers
    from dailySubCounts
    group by submission_date
)

select mHidD.submission_date, dnc.unqHackers, dsc.hacker_id, dsc.name
from minHidMaxSubCount as mHidD
left join dailySubCounts as dsc on mHidD.submission_date = dsc.submission_date and dsc.hacker_id = mHidD.minHid
left join dailyNumHackers as dnc on mHidD.submission_date = dnc.submission_date
order by mHidD.submission_date

2016-03-01 112 81314 Denise
2016-03-02 144 39091 Ruby
2016-03-03 122 18105 Roy
2016-03-04 136 533 Patrick
2016-03-05 144 7891 Stephanie
2016-03-06 140 84307 Evelyn
2016-03-07 101 80682 Deborah
2016-03-08 147 10985 Timothy
2016-03-09 154 31221 Susan
2016-03-10 108 43192 Bobby
2016-03-11 117 3178 Melissa
2016-03-12 107 54967 Kenneth
2016-03-13 90 30061 Julia
2016-03-14 146 32353 Rose
2016-03-15 117 27789 Helen


2016-03-01 112 81314 Denise
2016-03-02 59 39091 Ruby
2016-03-03 51 18105 Roy
2016-03-04 49 533 Patrick
2016-03-05 49 7891 Stephanie
2016-03-06 49 84307 Evelyn
2016-03-07 35 80682 Deborah
2016-03-08 35 10985 Timothy
2016-03-09 35 31221 Susan
2016-03-10 35 43192 Bobby
2016-03-11 35 3178 Melissa
2016-03-12 35 54967 Kenneth
2016-03-13 35 30061 Julia
2016-03-14 35 32353 Rose
2016-03-15 35 27789 Helen