select id, rental_date, payment_amount,
sum(payment_amount) over (order by rental_date)
from single_rental