# 윈도우 함수(Window Function)



### 1. Window Function이란?

MySQL이 가장 유명한 RDBMS가 된 이후, MySQL은 클라우드 기반의 DB시스템이 되었다. 그들이 쿼리 사용에 있어 수용량을 늘리기 위해서는, 쿼리의 확장성을 필요로 했는데 이 때문에 나온 것이 Window functions 이다.

> 그래서인지 MySQL version 8이상부터 적용된다.



윈도우 함수는 행과 행 간의 관계를 쉽게 정의하기 위해 만든 함수이다. 기존에 사용하던 집계 함수도 있고, 새로이 윈도우 함수 전용으로 만들어진 기능도 있다. 윈도우 함수는 OVER 문구 없이는 사용될 수 없다.

OVER에는 두 가지 사용법이 있는데,

- PARTITION BY - 순서를 재배치하기 위함.
- ORDER BY - 순서를 내림차순 혹은 오름차순 정렬하기 위함.



### 2. Different types of window functions

처음 나온 윈도우 함수는 집계(aggregate) 함수와 분석(analytical) 함수이다.

`집계` 함수는 그 이름처럼, 같은 그룹에 있는 것들의 계산 결과들을 제공한다.

> SUM, COUNT, AVG, MIN, MAX, return a scalar value



`분석` 함수는 랭킹(Ranking) 함수와 가치(Value) 함수 두 가지로 나누어 볼 수 있는데, 현재 행에 따라 레코드 창을 설정하고, 일반적으로 set of records를 출력한다.(?)

> RANK, DENSE_RANK, ROW_NUMBER, CUME_DIST, LAG, LEAD, etc.

<img src='https://www.devart.com/dbforge/mysql/studio/images/types-of-window-functions.png'></img>



