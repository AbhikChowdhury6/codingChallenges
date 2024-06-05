SELECT id, age, coins_needed, power FROM Wands
JOIN Wands_Property USING(code)
WHERE (age, coins_needed, power) IN

(SELECT age, MIN(coins_needed), power FROM
    (SELECT id, age, coins_needed, power, is_evil FROM Wands
    JOIN Wands_Property USING(code)) AS CombinedTable
WHERE is_evil = 0
GROUP BY power, age)

ORDER BY power DESC, age DESC 
