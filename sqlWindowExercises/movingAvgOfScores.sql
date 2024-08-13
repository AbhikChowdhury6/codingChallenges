select procedure_date, doctor_id, category, name, score,
avg(score) over (partition by category
                 order by procedure_date
                 rows between 2 preceeding and 3 following)
from procedures