'''
최소비용 문제
계단을 1칸 혹은 2칸씩 오른다고 할 때,
최소 비용으로 계단 오르기

입력
1) 계단의 갯수
2) 각 계단의 비용

출력
최소비용

5
10 15 20 25 30

40
'''

n = int(input())
costs = [0] + list(map(int, input().split()))

import math
dp = [0] + [math.inf for _ in range(n)]
steps = [1, 2]

for i in range(1, n+1):
    for step in steps:
        if i >= step:
            dp[i] = min(dp[i], dp[i-step]+costs[i])

result = dp[i]
print(result)