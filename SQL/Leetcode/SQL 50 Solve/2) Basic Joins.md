# [SQL 50solve](https://leetcode.com/studyplan/top-sql-50/)



## Basic Joins

#### Medium

- [Managers with at Least 5 Direct Report](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50)

```mysql
select name
from employee
where id in (select managerId 
            from employee
            group by managerId
            having count(managerId) > 4)
```



- [Confirmation Rate](http://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&envId=top-sql-50)

```mysql
/**
1) if user_id not in distinct(user_id) then 0
2) count
**/

select s.user_id, 
    round(sum(case when (c.action = 'confirmed') then 1 else 0 end) / count(*), 2) as confirmation_rate

from signups s left join confirmations c on s.user_id = c.user_id
group by s.user_id
```
