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



## Basic Aggregate Functions

#### Medium

```mysql
# Write your MySQL query statement below
select DATE_FORMAT(trans_date, '%Y-%m') as month, 
    country, 
    count(trans_date) as trans_count, 
    sum(if(state='approved', 1, 0)) as approved_count,
    sum(amount) as trans_total_amount, 
    sum(if(state='approved', amount, 0)) as approved_total_amount
from Transactions
group by month, country;
```



> GPT Feedback
>
> ```mysql
> SELECT 
>     DATE_FORMAT(trans_date, '%Y-%m') AS month,  -- Extract year and month from transaction date
>     country,  -- Country of the transaction
>     COUNT(*) AS trans_count,  -- Total number of transactions
>     SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,  -- Number of approved transactions
>     SUM(amount) AS trans_total_amount,  -- Total amount of all transactions
>     SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount  -- Total amount of approved transactions
> FROM Transactions
> GROUP BY month, country;  -- Group results by month and country
> ```
>
> 1) if 대신 Case when을 써주었다.
> 2) count(trans_date) 대신 count(*)을 써주는 게 더 직관적이라고 한다.
>
> 하지만 코드 자체의 가독성은 좋고 괜찮은 코드였다! (굿이에옹)



## Subqueries

#### Easy

- [Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50)

```mysql
# 말 그대로, Manager id에는 남아있지만, employee_id에는 없는 직원을 찾는코다.
select employee_id
from Employees
where manager_id not in (
    select employee_id
    from Employees
) and salary < 30000
order by employee_id asc;

## GPT를 통해 조건문을 조금 수정하자면 where절에 다음 한 줄을 넣어주는 게 좋다.
and manager_id is not NULL
```



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

- [Exchange Seats](https://leetcode.com/problems/exchange-seats/?envType=study-plan-v2&envId=top-sql-50)

```mysql
# Write your MySQL query statement below
# sol 1) switch id
select case
    when mod(id, 2)=0 then id-1
    when mod(id, 2)=1 and id+1 not in (select id from seat) then id # when the last id is odd
    else id+1 end as id,
    student
    from seat
    order by id

# sol 2) switch student
select id, 
    case when id%2=0 then (lag(student) over (order by id))
    else ifnull(lead(student) over (order by id), student)
    end as student
    from seat
```

```python
# using pandas
import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    result_df = seat
    
    df_odd = seat.iloc[0:len(seat)-1:2]
    df_even = seat.iloc[1::2]
    
    for i in range(len(seat)//2):
        result_df.at[i*2, 'student'], result_df.at[i*2+1, 'student'] = df_even.iloc[i].student, df_odd.iloc[i].student

    return result_df
```

> 홀수 아이디인 학생과 짝수 아이디인 학생의 위치를 바꾸는 문제.
>
> 처음에는 어떻게 해야 할 지 몰라 pandas로 먼저 풀고, solve를 찾아보았다.
>
> - 두 가지 접근법이 가능한데, 하나는 id를 바꿔주는 것, 다른 하나는 student를 바꿔주는 것
>
> 두 개 모두 좋은 솔루션이지만, 더 큰 데이터세트에서 좋게 사용하기 위해서는 Join을 사용해주는 게 좋다고 한다.

##### Solution 3: Using Join

```mysql
SELECT 
    s1.id, 
    IFNULL(s2.student, s1.student) AS student 
FROM 
    seat s1 
    LEFT JOIN seat s2 ON (s1.id % 2 = 1 AND s1.id + 1 = s2.id) OR (s1.id % 2 = 0 AND s1.id - 1 = s2.id)
ORDER BY s1.id;
```

> GPT 피드백
>
> #### 설명:
>
> 1. **JOIN**: `LEFT JOIN`을 사용하여 인접한 `id`를 기반으로 학생 이름을 교환합니다.
> 2. **IFNULL**: 홀수 인덱스의 마지막 학생이 짝을 찾지 못할 경우를 처리합니다.
>
> #### 최종 정리
>
> - **Solution 1**: 간결하지만 성능 저하 가능성.
> - **Solution 2**: 윈도우 함수를 사용하여 더 읽기 쉬운 코드. 그러나 큰 데이터 세트에서 성능 저하 가능성.
> - **Solution 3**: JOIN을 사용하여 최적화된 솔루션. 성능이 우수할 수 있으며, 특히 큰 데이터 세트에서 효율적입니다.
>
> 세 솔루션 모두 문제를 해결할 수 있지만, 데이터 크기와 환경에 따라 적절한 방법을 선택하는 것이 중요합니다.



- [Movie Rating](https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50)

```mysql
# Write your MySQL query statement below
with CTE as(
    select movie_id, user_id, rating, date_format(created_at, '%Y-%m') as created_at
    from MovieRating
),
movie_rating as(
    select title
    from CTE inner join Movies using (movie_id)
    where created_at = '2020-02'
    group by movie_id
    order by avg(rating) desc, title asc
    limit 1
),
user_count as(
    select name
    from CTE inner join Users using(user_id)
    group by user_id
    order by count(*) desc, name asc
    limit 1
)

select name as results from user_count
union all
select title as results from movie_rating
```

> GPT 피드백
>
> - 첫 CTE에서 모든 것을 불러오는 것보다 movie-rating과 user_count에서 필요한 것만 필터링하는 것이 효율적!
> - 쿼리는 효율적으로 잘 짜졌지만, using보다는 on을 써주어 명확하게 해주는 게 좋다고 한다.







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



#### Sorting and Grouping

- Customers Who Bought All products

```mysql
# Write your MySQL query statement below
with CTE as(
    select customer_id, count(distinct(product_key)) as cnt
    from Customer
    group by customer_id
    having cnt = 2
)

select customer_id
from CTE
```

> GPT-4o Self Feedback
>
> 내 풀이에서는, having 절에 2개의 품목을 바로 지정해주었는데, 저렇게 하면 품목이 바뀌는 경우 틀린 답이 되어버린다. 모든 제품에 대한 count 처리가 먼저 들어간 후, 그 값을 찾아야 한다.
>
> ```mysql
> WITH TotalProducts AS (
>     SELECT COUNT(*) AS product_count
>     FROM Product
> ),
> CustomerProductCount AS (
>     SELECT customer_id, COUNT(DISTINCT product_key) AS cnt
>     FROM Customer
>     GROUP BY customer_id
> )
> SELECT customer_id
> FROM CustomerProductCount, TotalProducts
> WHERE CustomerProductCount.cnt = TotalProducts.product_count;
> 
> ```

