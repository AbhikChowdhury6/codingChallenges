select id, procedure_date, name, price, 
lag(price) over (order by id) as previous_price,
price - lag(price) over (order by id) as difference
from procedures
