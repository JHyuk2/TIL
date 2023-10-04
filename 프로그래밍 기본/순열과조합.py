# permutation and combination 프로그래밍 하기

# 가장 기본적인 파이썬 구현 방법은 itertools 를 가져와 사용하는 것.

dataset = [i for i in range(10)]

# 여기서 4개의 숫자를 뽑아서 합이 10 이상인 경우만 보려고 한다.

from itertools import combinations

# 이렇게 전부 구하고 하는 건 메모리 낭비.
combi = list(combinations(dataset, 4)) 

print(combi)

## 1. bitwise 연산자를 사용하면 어떨까?

for i in range(len(dataset)):
    for j in range(1<<i):
        print(i&j)