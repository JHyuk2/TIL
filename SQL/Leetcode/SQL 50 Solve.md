# [SQL 50solve](https://leetcode.com/studyplan/top-sql-50/)



## Select

#### Easy

- [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/submissions/?envType=study-plan-v2&envId=top-sql-50)


```mysql
select tweet_id
from Tweets
where length(content) > 15
```





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



## Subqueries



#### Medium

- [Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/?envType=study-plan-v2&envId=top-sql-50)

```mysql
# 가장 많은 친구를 가진 사람이 누구인지를 뽑기 위함.
# 요청을 가장 많이 한 사람 + 요청을 가장 많이 받은 사람.
-- primary key가 순열이 아닌 조합쌍으로 이루어져있기 때문에, 중복이 될 수 없다. 

# 1) 친구에게 요청을 가장 많이 한 사람.
select requester_id as id,
    (select count(*) 
    from RequestAccepted  
    where requester_id = id or accepter_id = id) as num    
from RequestAccepted
group by requester_id 

union 
 
# 2) 가장 많은 요청을 받은 사람.
select accepter_id as id,
    (select count(*) 
     from RequestAccepted  
     where requester_id = id or accepter_id = id) as num
from RequestAccepted
group by accepter_id

# 3) 둘을 내림차순으로 정렬 후 1명만 뽑기.
order by num desc
limit 1; 
```



> 다른 사람의 코드를 보니, 훨씬 더 복잡도를 줄일 수 있는 방법이 있었다...

#### Complexity

- Time complexity

- Space complexity

```mysql
# Write your MySQL query statement below
with base as(select requester_id id from RequestAccepted
union all
select accepter_id id from RequestAccepted)


select id, count(*) num  from base group by 1 order by 2 desc limit 1
```

> 그냥 다 더해버리면 그만이니까. 이런 방법도 있다.

