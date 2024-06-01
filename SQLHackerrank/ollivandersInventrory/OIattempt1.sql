-- WITH table1 AS
SELECT w.id,  wp.age, w.coins_needed, w.power FROM Wands w
JOIN Wands_Property wp ON w.code = wp.code
WHERE wp.is_evil = 0

/* get the wand id's with the lowest price per grouping*/
/*
table2 AS
(SELECT id FROM table1
GROUP BY age, power)

SELECT * FROM table2
*/


/*
SELECT wp.age, MIN(w.coins_needed), w.power FROM Wands w
JOIN Wands_Property wp ON w.code = wp.code
WHERE wp.is_evil = 0
GROUP BY wp.age, w.power
ORDER BY w.power DESC, wp.age DESC 
*/