-- I am a bit unsure if putting the window function directly 
-- in the where claues works
select c.first_name, c.last_name, g.payment_date
from customer c join giftcards g
on c.id = g.customer_id
where row_number() over (
    order by g.payment_date desc
) = 2;

--remember
--the default partition is every row
--the deafult window is unbounded preceeding


-- using a subtable seems cleaner
with ranks as (
    select c.first_name, c.last_name, g.payment_date,
    row_number() over (
        order by g.payment_date desc
    ) as rank
    from customer c join giftcards g
    on c.id = g.customer_id
)

select first_name, last_name, payment_date
from ranks
where rank = 2;