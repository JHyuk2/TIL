# 다이나믹 프로그래밍

- 다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간을 비약적으로 증가시키는 방법
- 이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.
- 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식으로 구성된다.
  - 탑다운 - 메모이제이션
  - 바텀업

- 동적 계획법이라고 부르는데, 여기서 다이나믹은 별다른 의미 없이 사용된 언어이다.
  - 동적 할당은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미한다.



## 다이나믹 프로개리믕의 조건

1. 최적 부분 구조(Optimal Substructure)
   - 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
2. 중복되는 부분 문제 (Overlapping Subproblem)
   - 동일한 작은 문제를 반복적으로 해결해야 한다.



즉, 점화식으로 표현될 수 있는가?

ex) 피보나치 수열 (An = An-1 + An-2, A1=1, A2=2) 



![fibo](fibo.jpg)

함수로 표현을 하게 되면

```python
# 함수표현 피보나치 수열
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))
```

하지만 함수의 함수의 함수의 함수의 ....를 계속 호출하기때문에 메모리사용측면에서 불리하다.



### 메모이제이션

- 메모이제시연슨 다이나믹 프로그래밍을 구현하는 방법 중 하나로,
- 한번 계산한 결과를 메모리 공간에 메모하는 기법이다.
  - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져온다.
  - 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 한다.



### 탑다운  vs 바텀업

- 탑다운(메모이제이션) 방식은 하향식이라고도 하며 바텀업 방식은 상향식이라고 한다.
- 다이나믹 프로그래밍의 전형적인 형태는 바텀업 형식이다.
  - 결과 저장용리스트는 DP (dynamic programming) 테이블이라고 부른다.
- 엄밀히 말하면 메모이제이션은 `이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념`을 의미
  - 따라서 메모이제이션은 DP에만 국한된 개념은 아니다.



> 맨 마지막 실행할 함수=(An)를 먼저 확인한 후, 점화식의 값을 호출하는 방식

```python
# 탑다운 다이나믹 프로그래밍 피보나치 수열
d = [0] * 100 # DP 테이블 - 메모이제이션을 위한 리스트

def fibo(x):
    # 종료 조건
    if x==1 or x==2:
        return 1

    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산한 적이 없는 문제라면 점화식에 따라 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
```

> 앞에서부터 차곡차곡 채워나가는 방식 | (재귀함수를 거의 필요로하지 않는다.)

```python
# 바텀업 다이나믹 프로그래밍 피보나치 수열 
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
   
print(d[n])
```

탑다운 방식이 수학적으로 직관적이고 이해하긴 쉽지만, 메모리나 스택오버플로의 영역에선 불리할 수 있다.

(대부분 실제로는 거의 비슷하다.)![fibo_effect](fibo_effect.jpg)

> 시간복잡도가 O(N)이 된다.



## 다이나믹 프로그래밍 VS 분할 정복

- 다이나믹 프로그래밍과 분할 정복은 모두 최적 부분 구조를 가질 때 사용할 수 있다.
  - 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아 큰 문제를 해결할 수 있다.
- 다이나믹 프로그래밍과 분할 정복의 차이점은 `부분 문제의 중복`
  - DP는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복
  - 분할 정복은 동일한 부분 문제가 반복적으로 계산되지 않는다.



### 분할 정복 - 퀵 정렬(Quick Sort)

> 한 번 기준 원소가 자리를 변경해서 자리를 잡으면 그 기준 원소의 위치는 바뀌지 않는다.
>
> 분할 이후 해당 피벗 값을 다시 처리하는 부분 문제는 호출하지 않는다.



### 문제접근 방법

- 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지를 검토한다.
  - 다른 알고리즘으로 풀이 방법이 떠오르지 않는다면 DP 를 고려해야 한다.
- 일단 재귀함수로 비효율적인 완전 탐색을 작성한 뒤(탑다운) 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있다면, 코드를 개선하는 방법을 사용할 수 있다.
- 일반적인 코테는 기본 유형의 DP문제가 출제되는 경우가 많다.



###### <문제> 개미 전사

```python
# 백준 / 프로그래머스 중에 있는듯.

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])
    
print(d[n-1])
```



###### <문제> 1로 만들기

```python
# 백준 / 프로그래머스 중에 있는듯.

X = int(input())
d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i-1] + 1
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] +1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] +1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] +1)        
          
print(d[x])
```



그 외

###### 효율적인 화폐 구성, 금광, 병사 배치하기
