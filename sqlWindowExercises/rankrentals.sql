select mv.title, mv.genre, sr.payment_amount,
rank() over (partition by mv.genre
             order by sr.payment_amount desc)
from single_rental sr join movie mv
on  sr.movie_id = mv.id;

--remember
--row_number() is straightforward
--rank() is row_number() but with ties
    --being the lowest row number (ranks the rows)
--dense_rank() is what ranks the values