# [SQL 50solve](https://leetcode.com/studyplan/top-sql-50/)



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



- customer who bought all products

> ```mysql
> select customer_id
> from Customer
> group by customer_id
> having count(distinct(product_key)) = (
>     select count(*)
>     from Product
> )
> ```
>
> 다시 풀어보니 훨씬 잘된다..!
>
> 
>
> 친절한 GPT에게 물어보니, 코드는 잘 짰는데, 가독성을 늘려보는 게 어떻냐고한다.
>
> ```mysql
> -- Subquery to get the total number of unique products
> WITH TotalProducts AS (
>     SELECT COUNT(*) AS total_count
>     FROM Product
> )
> 
> -- Main query to find customer IDs who bought all products
> SELECT customer_id
> FROM Customer
> GROUP BY customer_id
> HAVING COUNT(DISTINCT product_key) = (SELECT total_count FROM TotalProducts)
> 
> ```
>
> 결과는 동일하나 가독성이 나아진 점은 인정이다...



- Restaurant Growth

```mysql
# Write your MySQL query statement below
with CTE as(
    select visited_on, sum(amount) as total
    from Customer
    group by visited_on
)

select visited_on,
    sum(total) over(order by visited_on ASC rows between 6 preceding and current row) as 'amount',
    avg(total) over(order by visited_on ASC rows between 6 preceding and current row) as 'average amount'
    from CTE
    where DATE_SUB(visited_on, interval 6 day) in (select visited_on from CTE)
```

> Moving Average를 구현해야 하는 문제이다.
>
> 총 금액과 이동평균을 나타내는 방법을 생각해보자.
>
> <총 금액 구하기>
>
> 1. group by로 날짜별로 묶어주고, 현재일자로부터 7일 이전까지 합계 구하기
> 2. 

```mysql
WITH TotalAmount AS (SELECT visited_on,
sum(amount) as total
FROM Customer
GROUP BY visited_on)

SELECT visited_on, amount, average_amount
FROM (SELECT visited_on,
sum(total) over(order by visited_on ASC rows between 6 preceding and current row) AS 'amount',
round(avg(total) over(order by visited_on ASC rows between 6 preceding and current row), 2) AS 'average_amount'
FROM TotalAmount) AS Temp
WHERE DATE_SUB(visited_on, INTERVAL 6 DAY) IN (SELECT visited_on FROM TotalAmount)
ORDER BY visited_on ASC
```

