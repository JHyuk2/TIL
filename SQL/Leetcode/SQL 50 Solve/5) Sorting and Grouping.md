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

