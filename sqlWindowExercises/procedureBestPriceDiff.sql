select procedure_date, name, price, category, score,
min(price) over (partition by category
                 rows between unbounded preceeding
                 and unbounded following) as best_procedure,

price - best_procedure as difference
from procedures

--I misread the instructions again
--we take the price of the highest scored procedure

select procedure_date, name, price, category, score,
first_val(price) over (
    partition by category
    order by score desc
) as best_procedure,
price - best_procedure as difference

from procedures


-- remember first_value(of a column)
-- is handy with order by's to get max's and min's
-- based on other columns 