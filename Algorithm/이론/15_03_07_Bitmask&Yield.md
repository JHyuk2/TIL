# Bitmask & Yield

조합, 순열, 부분집합을 만들 수 있는 방법은 다양하다.

이번에는 그 중 가장 깔끔하고, 메모리를 효율적으로 사용하는 방법 두 가지인

1) `비트마스킹(bitmasking)`과 2) `yield` 함수에 대해서 정리해보았다.



## # 1. Bitmask를 이용한 멱집합(부분집합) 구하기

`멱집합`은 모든 부분집합의 집합(Power set)을 의미한다.

s = {1, 2, 3, 4, 5}일 때 power set의 개수는 2^5, 즉 32개이다.

수학적으로 증명하자면 모든 부분집합은 각 원소에 대해 두 가지 선택지가 존재한다.

- 1) 원소를 포함한다.

- 2) 원소를 포함하지 않는다.

즉 set을 만들 수 있는 모든 가지수는 각 원소에 대해 고르느냐 안고르느냐를 정하는 것으로 부분집합을 결정할 수 있다.

(**물론 이런 접근을 하면 nCr 과 동치이므로 5C2 조합으로 충분히 가능**하긴 하지만, 비트마스킹을 사용해보자.)



### # # 1-1) def powerset

```python
def powerset(s):
	masks = [ 1 << i for i in range(len(s)) ]
	for i in range( 1 << len(s) ):
		yield [ss for ss,mask in zip(s,masks) if mask & i ]
```

굉장히 짧게 생성이 가능한데, 출력 결과를 확인하면 다음과 같다. 

```python
for power in powerset([1,2,3,4,5]):
    print(power)
    
>>
[]
[1]
[2]
[1, 2]
[3]
[1, 3]
[2, 3]
[1, 2, 3]
...
[3, 4, 5]
[1, 3, 4, 5]
[2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

이제, 코드를 한 줄씩 살펴보도록 하자



### # # 1-2) shift 연산자를 이용한 mask 생성

```python
masks = [1 << i for i in range(len(s))]
```

`<< (쉬프트 연산자)`는 이진수의 자리수를 왼쪽으로 밀어주는 연산자로, 다음처럼 계산된다.

1 << 0  = bin(1)

1 << 1 =  bin(10)

1 << 2 =  bin(100)

**십진법으로는 현재 숫자에 2를 곱해주는 계산**이 되므로, **masks = [1, 2, 4, 8, 16]** 이 된다.



### # # 1-3) 2^n 만큼 반복하기

```python
for i in range( 1 << len(s) ):
```

1 << len(s) 만큼 반복한다 == 부분집합을 만들 수 있는 경우의 수인 **2^n 만큼 반복**한다는 뜻이다.

이제 마지막 줄만 해석을 하면 된다.



```python
yield [ss for ss,mask in zip(s,masks) if mask & i ]
```

yield 함수는 return과는 다르게 generator를 통해 값을 생성해주는 함수이다.

yield에 대해서는 하단부 2에서 다뤄보기로 하고, 이어지는 줄부터 보자.

s = [1,2,3,4,5]

makss = [1, 2, 4, 8, 16] 이 들어있었다.

이를 집 함수로 묶어준 zip에는 각각 [(1, 1), (2, 2), (3, 4), (4, 8),  (5, 16)] 이란 값이 들어오게 된다.

이 때 mask와 i가 같게 되면 yield하라는 함수가 생성되고, 그를 통해 power set을 구현할 수 있게 된다.

아직 아리송할 것이다...



**아래를 통해 조금 더 알아보자!**

### # # 1-4) and 연산자에 대한 추가 설명

먼저 ss, mask을 zip값을 통해 보면 [(1, 1), (2, 2), (3, 4), (4, 8),  (5, 16)]  임을 알 수 있다.

이 때 mask & i 인 경우, ss를 담는 리스트를 생성하는데, 

이 부분 역시 비트연산자의 앤퍼샌드(&)를 사용하면 쉽게 구현이 가능하다.

> (1-2) 참고

&는 두 개의 이진수 a, b가 같은 자리수가 1인 경우만 1, 나머지는 0으로 반환한다.

간단한 예시로 a == 5, b ==4 라고 보자.

bin(a) = 1001 이란 값이 나오게 되는데, 

bin(b) = 1000

----------------------

a&b = 1000 이 되는 것이다. 



즉, 위와 비슷하게 i = 13이라고 가정해보면

bin(13) = 1101 로 표시되고, 이는 4, 3, 1번째 값을 담고 있는 부분집합과 동일하다고 볼 수 있다.

그 때 ss값들의 리스트는 [1, 4, 8] 이 만들어진다.



# #  2. Generator - Yield

Yield는 return과 다르게 함수를 진행하면서 나올 수 있는 값들을 generator에 저장하여 하나씩 추가한다.

파이썬 코드를 통해 비교를 해보면 조금 더 보기 편하다.

**1) return**

```python
# return
def generator():
    for i in range(10):
        return i

print(generator())
>> 0
```

**2) yield**

```python
# yield
def generator():
    for i in range(10):
        yield i
        
print(generator())
>> <generator object generator at xxxxxx>
```

제네레이터는 일종의 시퀀스형 자료형으로 iterable한 객체로 정의된다.

이를 list로 형변환해서 찍어보면 [i for i in range(10)] 과 동일한 객체임을 알 수 있다.



> yield는 그럼 왜 사용할까?
>
> yield generator는 **함수를 호출할 때마다 값을 하나씩 보내준다.** 
>
> 즉 i라는 값을 호출 가능한 횟수가 남아있으면 계속해서 호출 후 끝나면 소멸된다.



그럼 이제 마지막줄을 다시 보면 이해하기가 조금 쉽다.

```python
for i in range( 1 << len(s) ):
    yield [ss for ss,mask in zip(s,masks) if mask & i ]
```

i = 0 부터 시작할 땐 빈 리스트를 generator에 추가,

i = 1 -> [1]

i = 2 -> [2]

...

이렇게 쭉 값을 generator에 담게 되고, 함수의 호출 가능 횟수가 종료되면 generator를 반환하게 된다.



## # 3. 순열, 조합, 중복조합 구현

위에 yield를 활용하여 조합을 먼저 구현해보자.

return을 사용할때와 다르게 굉장히 편하고 간결한 코드로 구현이 가능하다.



**n개 중 r개를 뽑는 combinations**

```python
def combinations(arr,r):
    for i in range(len(arr)):  // 함수에서 지금할 일
        if r == 1:  // 종료조건
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1): // 다음에 할 일
                yield [arr[i]] + next

for combi in combinations([1,2,3,4,5],2):
    print(combi)
```



~~다음 내용은 피곤해서 나중에 작성한다~~

