select sum(ci.POPULATION)
from CITY as ci
join COUNTRY as co on co.CODE = ci.COUNTRYCODE
where co.CONTINENT = 'Asia'