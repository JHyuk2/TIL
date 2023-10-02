# Initial EDA 



## Validating 

1. Check type ~ Updating data types, categorical data

   - pd.DataFrame.info()
   - pd.DataFrame.describe()
   - pd.DataFrame.shape

2. Filtering ~ using boolean filter(w/ `isin()` method)

3. sns.boxplot(x='@data', y='@category')

   - use seaborn.boxplot ~ outlier check

   ```python
   ## unemployment의 데이터에서 2021년의 취업률을 대륙별(continent)로 나누어
   # boxplot으로 4분위수를 보고 싶은 경우,
   
   import pandas as pd
   import seaborn as sns
   import matplotlib.pyplot as plt
   
   #--- 가상의 데이터셋 unemployment 존재
   # unemployment = pd.read_csv(@'unemployment 경로')
   sns.boxplot(data=unemployment, x='2021', y='continent')
   plt.show()
   ```



## Data summarization

1. groupby

   특정 값에 따라 Data aggregation이 가능하다.

   ```python
   books.groupby('genre').mean()
   ```

   - Sum: `.sum()`
   - Count: `.count()`
   - Minimum: `.min()`
   - Maximum: `.max()`
   - Variance: `.var()`
   - Standard deviation: `.std()`

   

   이 모든걸 한방에 해결해주는 `.agg()` 가 있다.

   ```python
   # 한 번에 여러 가지를 표현하고 싶은 경우
   books.agg(['mean', 'std'])
   
   # 각각의 컬럼마다 다른 aggregation을 적용하고 싶을 때
   books.agg({'rating': ['mean', 'std'], 'year': ['median']})
   
   # groupby와 활용하여 아래와 같이 튜플과 묶어 새로운 컬럼으로 정리할 수 있다.
   books.groupby('genre').agg(
   	mean_rating=('rating', 'mean'),
       std_rating=('rating', 'std'),
       median_year=('year', 'median')
   )
   
   # sns.barplot을 활용하면 mean값을 알아서 계산해주고 시각화해준다.
   # 막대 그래프는 평균에 대한 95% 신뢰 구간을 상단의 수직선으로 표시한다.
   sns.barplot(data=books, x='genre', y='rating') 
   plt.show()
   
   ## groupby('genre').agg({'rating':['mean']}) 이거랑 비슷하다.
   ## groupby('genre')['rating'].mean() 이거와도 비슷한 결과
   
   ```
