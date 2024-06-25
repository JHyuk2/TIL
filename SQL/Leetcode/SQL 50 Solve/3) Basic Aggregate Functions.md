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



#### Medium

```mysql
# Write your MySQL query statement below
with CTE as (
    select customer_id, min(order_date) as order_date, min(customer_pref_delivery_date) as delivery_date
    from Delivery
    group by customer_id
)

select 
    round(sum(case when order_date = delivery_date then 1 else 0 end) / count(*) * 100, 2) as immediate_percentage
    from CTE
```

> GPT Feedback
>
> ```mysql
> WITH CTE AS (
>     SELECT customer_id, MIN(order_date) AS first_order_date
>     FROM Delivery
>     GROUP BY customer_id
> ),
> FirstOrders AS (
>     SELECT d.delivery_id, d.customer_id, d.order_date, d.customer_pref_delivery_date
>     FROM Delivery d
>     INNER JOIN CTE c ON d.customer_id = c.customer_id AND d.order_date = c.first_order_date
> )
> SELECT 
>     ROUND(
>         SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*) * 100, 2
>     ) AS immediate_percentage
> FROM FirstOrders;
> ```
>
> ### 잘한 점:
>
> 1. **CTE 사용**: CTE를 사용하여 각 고객의 첫 주문을 선택하는 부분이 적절합니다.
> 2. **조건부 합산**: `CASE` 문을 사용하여 즉시 주문인지 확인하는 부분이 잘 구현되었습니다.
> 3. **비율 계산**: 비율을 계산하고 소수점 두 자리로 반올림하는 부분도 적절하게 작성되었습니다.
>
> ### 아쉬운 점:
>
> 1. **첫 주문 날짜 계산**: `min(order_date)`만 사용해야 하는데, `min(customer_pref_delivery_date)`를 추가로 사용하여 잘못된 결과가 나올 수 있습니다.
> 2. **조건부 합산 및 비율 계산**: 비율 계산이 정확하지 않을 수 있습니다. 정확성을 높이기 위해 `sum`과 `count`를 분리하여 계산하는 것이 좋습니다.
>
> ### 제안할 점:
>
> 1. **CTE에서 첫 주문 날짜만 선택**: 각 고객의 첫 주문 날짜만 선택하도록 수정합니다.
> 2. **CTE와 원본 테이블 결합**: 첫 주문 날짜를 기준으로 원본 테이블과 결합하여 첫 주문의 세부 정보를 가져옵니다.
> 3. **비율 계산**: 조건부 합산 및 비율 계산을 분리하여 정확성을 높입니다.
>
> ---
>
> First Orders를 사용하는 의도는 알겠는데, 오히려 저게 가독성을 떨어뜨리는 거 아닌가...?
>
> 결과는 같은데 결국 min을 두 개 다 쓰는게 더 좋았던 거 같다. (내생각)

