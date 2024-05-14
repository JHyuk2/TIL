#  Joining Data With Pandas



## 1. Data Merging Basics

### 1) Inner Join

가장 기본적인 조인문, merge 함수

```python
wards_census = wards.merge(census, on="ward")
print(wards_census.head())
```

#### Suffixes

```python
wards_census.columns
```

병합된 테이블에 _x, _y와 같은 접미사가 붙음.

```python
# suffix 제어
wards_census = wards.merge(census, on="ward", suffixes=("_ward", "_cen"))
print(wards_census.head())
print(wards_census.shape)
```



### 2) One-to-One / One-to-Many relationships

#### table.1 (Left table)

| A    | B    | C    |
| ---- | ---- | ---- |
| A1   | B1   | C1   |
| A2   | B2   | C2   |
| A3   | B3   | C3   |

#### # table.2 (Right table)

| C    | D    |
| ---- | ---- |
| C1   | D1   |
| C1   | D2   |
| C1   | D3   |
| C2   | D4   |

#### One-to-Many = Every row in left table is related to one or more rows in the right table



#### 3) Merging multiple DataFrames



## 2. Merging Tables With Different Join Types





## 3. Advanced Merging and Concatenating



## 4. Merging Ordered and Time-Series Data



