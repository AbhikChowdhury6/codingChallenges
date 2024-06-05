SELECT id, t2.age, coins_needed, t1.power FROM wands AS t1,
(
    SELECT age, w.code, power, MIN(coins_needed) as min_coins FROM wands as w
    INNER JOIN wands_property as wp
    ON w.code = wp.code AND is_evil = 0
    GROUP BY power, age, w.code
) AS t2
WHERE t1.code = t2.code AND t1.power = t2.power AND t1.coins_needed = t2.min_coins
ORDER BY power DESC, age DESC
/*
you can select columns from a set of tables, seperated like how columns are seperated
you can combine this with defining tables using subqueries in parenthesis and aliasing them
*/

SELECT W.id, WP.age, W.coins_needed, W.power FROM Wands W 
JOIN Wands_Property WP ON W.code = WP.code 
WHERE WP.is_evil = 0 AND
 W.coins_needed = 
 ( SELECT MIN(W1.coins_needed) FROM Wands W1 
 WHERE W1.code = W.code AND W1.power = W.power )  --the element returned by this query
ORDER BY W.power DESC, WP.age DESC;
/*
I think they might have been able to use either
min w1 coins needed or min w coins needed
*/



 select id,age,coins_needed,power from wands as w 
 inner join wands_property as wp using(code) 
 where is_evil = 0 and 
 (age,coins_needed,power) IN 
    ( select age, min(coins_needed),power from wands as w 
    inner join wands_property as wp using(code) 
    where is_evil = 0 
    group by power,age )
order by power desc , age desc;

/*
what is this set IN notation

why aren't they adding table prefixes to their column names
*/

/*
interesting notes
    - you can group column names using parenthesis
    - you can make a subquery anywhere with parenthesis
    - in a group by you can only return columns that are in the groupby or aggregates
    - you can use the using keyword to join with a column name aparently
    - join and inner join are the same
        - they both only return rows with values found in both tables
    - you can use AS to alias columns as well as table names
        - the word AS literally can be ommitted rippp
    - left or right outer join will include all join keys in the 
        left or right table setting the values to the unmatched 
        rows to NULL
    - Full join is the left and right join together

*/