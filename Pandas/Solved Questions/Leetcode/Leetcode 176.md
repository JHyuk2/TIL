## LeetCode Problem List (w/ Pandas)

### 176. Second Highest Salary

```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 중복 제거
    df = employee.drop_duplicates(['salary'])

    if len(df) == 1:
        return pd.DataFrame([{'SecondHighestSalary': None}])

    df = df.sort_values(by='salary').tail(2).head(1).
    rename(columns = {'salary': 'SecondHighestSalary'})
```



---

### Self Feedback(w/ GPT-4o)

주어진 코드는 이미 효율적이고 간결하지만, 몇 가지 사소한 수정으로 가독성을 더욱 향상시킬 수 있습니다. 예를 들어, `tail`과 `head`를 사용한 슬라이싱을 한 줄로 줄이고, `rename`을 사용하는 부분을 명확히 할 수 있습니다.



```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 중복 제거
    df = employee.drop_duplicates(['salary'])

    if len(df) < 2:
        return pd.DataFrame([{'SecondHighestSalary': None}])

    # 정렬 후 두 번째 높은 급여 찾기
    second_highest = df.nlargest(2, 'salary').iloc[-1]['salary']
    
    return pd.DataFrame([{'SecondHighestSalary': second_highest}])

# 예제 데이터
data = {'id': [1, 2, 3], 'salary': [100, 200, 300]}
employee = pd.DataFrame(data)

# 결과 출력
print(second_highest_salary(employee))
```



### 개선된 코드 설명:

1. **중복 제거**: `drop_duplicates` 메서드를 사용하여 중복된 급여를 제거합니다.
2. **조건 확인**: 중복 제거 후, 데이터프레임의 길이가 2보다 작은 경우, 두 번째 높은 급여가 없으므로 `None`을 반환합니다.
3. **두 번째 높은 급여 찾기**: `nlargest` 메서드를 사용하여 상위 2개의 급여를 찾고, 그 중 두 번째로 높은 급여를 선택합니다.
4. **결과 반환**: 두 번째 높은 급여를 포함하는 데이터프레임을 반환합니다.

이 코드의 시간복잡도는 여전히 O(N log N)이며, 공간복잡도는 O(N)입니다. 코드의 가독성과 효율성을 모두 유지하면서 개선하였습니다.

