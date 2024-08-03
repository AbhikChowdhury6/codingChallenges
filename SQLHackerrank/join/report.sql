SELECT if(g.Grade>7, s.Name, NULL), g.Grade, s.Marks
FROM Students as s join Grades as g 
on s.Marks Between  g.Min_Mark and g.Max_Mark

ORDER BY g.Grade DESC, s.Name