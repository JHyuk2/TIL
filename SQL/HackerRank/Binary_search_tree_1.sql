select N, case
    when P is null then 'Root'
    when N in (select P from BST where P is not null) then 'Inner'
    else 'Leaf'
    end as NodeType
from BST
order by N;