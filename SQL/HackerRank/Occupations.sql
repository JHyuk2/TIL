/*
Enter your query here.
*/

select 
    max(case when occupation='Doctor' then name end) as Doctor,
    max(case when occupation='Professor' then name end) as Professor,
    max(case when occupation='Singer' then name end) as Singer,
    max(case when occupation='Actor' then name end) as Actor
from (
    select 
        name, 
        occupation,
        row_number() over (partition by occupation order by name) as rn
    from occupations
) as sub
group by rn
order by rn;
