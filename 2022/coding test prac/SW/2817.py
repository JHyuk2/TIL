# 부분집합의 합 구하기
# input을 받는 방법은 두 가지가 있음.
# 1. 반복문을 사용한 input().split()을 사용하는 방법.
# 예시) data = list(map(int, input().split()))

# 2. sys.stdin.readline() 을 사용하는 방법
# 예시) list(map(int, sys.stdin.readline().split()))

# 여기서 map을 사용해주는 이유는 object 타입으로 리턴하기 때문에, list로 바꿔줌.
# 실제 문제를 풀 때는 2번을 사용해야 시간 초과가 발생하지 않음.

'''
- sample_input.txt - 
1
4 3
1 2 1 2 
1 2 3 4
'''

import sys

sys.stdin = open('./coding test prac/SW/2817_sample.txt') # 로컬환경에서만 사용

data = list(map(int, sys.stdin.readline().split()))
print(data)