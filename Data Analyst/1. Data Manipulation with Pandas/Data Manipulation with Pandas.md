# 1. Data Manipulation with pandas



##  1) Introducing DataFrames

"표 형식 데이터" 라고 불리는 가장 일반적인 형식의 직사각형 데이터를 사용한다.



### 데이터 확인을 위한 기본 문법

```python
import pandas as pd

# 데이터 불러오기
dogs = pd.read_csv("dataset/dogs.csv")

# 상위/하위 5개 출력
dogs.head()
dogs.tail()

# 기본 정보 확인 - info, describe, shape
dogs.info()
dogs.describe()
dogs.shape # <-- method가 아니라 attribute이다.

# columns, index, values
dogs.values # <-- 2차원 Numpy 배열의 데이터 값을 포함하여 제공
dogs.columns # <-- 열 이름 // Index(['name', 'phone_num'], dtype='object')
dogs.index # <-- 행 번호, 행 이름 // RangeIndex(start=0, stop=7, step=1)
```



## 2. Sorting and subsetting

데이터 정렬과 서브셋



### Sorting

```python
# column을 기준으로 하는 정렬
dogs.sort_values('weight_kg', ascending=False) # 오름차순 정렬 해제
dogs.sort_values(['weight_kg', 'height_cm']) # 여러 변수 기준 정렬

# 각각에 대해서 오름차순 내림차순 적용도 가능하다.
dogs.sort_values(['weight_kg', 'height_cm'], ascending=[True, False])
```



### Subsetting

```python
# 단일 컬럼
dogs["name"]
dogs.name # <-- 단, 컬럼 이름에 공백이 없어야 함.

## 다중 컬럼
# 방법1
dogs[["breed", 'height_cm']]
# 방법2
cols_to_subset = ["breed", 'height_cm']
dogs[cols_to_subset]

## 필터링 논리 조건 만들기
dogs["height_cm"] > 50
dogs[dogs["height_cm"] > 50]
dogs[dogs["breed"] == "Labrador"]
dogs[dogs["date_of_birth"] < "2015-01-01"]

# 여러 조건을 다중으로 걸기
is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["color"] == "Brown"
dogs[is_lab & is_brown] ## and, or 연산자 등을 사용할 수 있다.

# isin() 을 사용한 필터링
is_balck_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]
```

