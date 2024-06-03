/*
Enter your query here. 25.0735
*/

set @rc = (select ceil((select count(*) from station) /2) from station limit 1);
set SQL_SELECT_LIMIT = cast(@rc as unsigned);

with halfStations as (
    select * from station  
    order by lat_n)

select round(lat_n, 4) from halfStations limit 1





