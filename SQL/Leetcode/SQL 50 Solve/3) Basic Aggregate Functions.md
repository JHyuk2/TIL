# [SQL 50solve](https://leetcode.com/studyplan/top-sql-50/)



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


