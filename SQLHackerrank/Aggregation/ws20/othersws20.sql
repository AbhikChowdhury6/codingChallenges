DECLARE @row_cnt int = (SELECT COUNT(LAT_N) FROM STATION);

IF @row_cnt % 2 = 0 BEGIN 
    SELECT FORMAT(AVG(LAT_N), '#####.####') FROM 
        ( SELECT LAT_N FROM STATION ORDER BY LAT_N OFFSET @row_cnt / 2 ROWS FETCH NEXT 2 ROWS ONLY ) as median_rows 
    END 
ELSE BEGIN 
    SELECT FORMAT(LAT_N, '#####.####') FROM STATION ORDER BY LAT_N OFFSET @row_cnt / 2 ROWS FETCH NEXT 1 ROW ONLY 
    END



WITH cte1 AS(
SELECT
    CAST(
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY LAT_N) OVER ()
    AS DECIMAL(10,4)
        ) AS median
FROM station)

SELECT 
    MAX(median)
FROM cte1;


with stationWithRows as
    ( select lat_n, row_number() over (order by lat_n) row_n from station ) 

select round(lat_n, 4) from stationWithRows 
join ( select avg(row_n) medianRow from stationWithRows ) agg 
on agg.medianRow=row_n


SELECT ROUND(AVG(LAT_N),4) FROM 
    (SELECT *, 
        ROW_NUMBER () OVER(ORDER BY LAT_N) AS RN,
        COUNT(1) OVER() AS CNT 
        FROM STATION) A 
WHERE RN BETWEEN CNT/2 AND CNT/2+1;


SET @row_count = (SELECT CAST(FLOOR(COUNT(*) / 2) AS SIGNED) FROM STATION);
PREPARE STMT FROM "SELECT ROUND(LAT_N, 4) FROM STATION ORDER BY LAT_N LIMIT 1 OFFSET ? ";
EXECUTE STMT USING @row_count;


WITH sorted_values AS ( SELECT LAT_N FROM STATION ORDER BY LAT_N )
SELECT ROUND( CASE -- If the count is odd, select the middle value 
    WHEN (SELECT COUNT() FROM sorted_values) % 2 = 1 
        THEN ( SELECT LAT_N FROM 
            ( SELECT LAT_N, ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num FROM sorted_values ) AS numbered 
        WHERE row_num = (SELECT (COUNT() + 1) / 2 FROM sorted_values) ) -- If the count is even, average the two middle values 
    ELSE ( SELECT AVG(LAT_N) FROM ( SELECT LAT_N, ROW_NUMBER() 
        OVER (ORDER BY LAT_N) AS row_num FROM sorted_values ) AS numbered 
            WHERE row_num IN ( (SELECT COUNT() / 2 FROM sorted_values), (SELECT COUNT() / 2 + 1 FROM sorted_values) ) ) END, 4) AS median;







