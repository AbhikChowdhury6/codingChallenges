select mv.title, mv.genre, sr.payment_amount,
rank() over (partition by mv.genre
             order by sr.payment_amount desc)
from single_rental sr join movie mv
on  sr.movie_id = mv.id;