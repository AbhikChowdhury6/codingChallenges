/*
you could also use LEFT(CITY, 1) instead of SUBSTR
*/
SELECT DISTINCT CITY FROM STATION
WHERE 
SUBSTR(CITY, 1, 1) = 'A' or
SUBSTR(CITY, 1, 1) = 'E' or
SUBSTR(CITY, 1, 1) = 'I' or
SUBSTR(CITY, 1, 1) = 'O' or
SUBSTR(CITY, 1, 1) = 'U' 