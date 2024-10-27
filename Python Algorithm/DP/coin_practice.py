'''
동전의 종류가 주어졌을 때,
거스름을 최소한의 동전으로 계산하는 방법

1 - 사용할 수 있는 동전의 종류
2 - 손님이 받아야 할 거스름돈
출력 - 총 사용된 동전의 개수

3
1 2 5
11

3
'''

n = int(input())
coins = list(map(int, input().split()))
target = int(input())

import math
dp = [math.inf for _ in range(target+1)]
# 초기 설정
dp[0] = 0

for i in range(1, target+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin]+1)

result = dp[target]
print(result if result != math.inf else -1)  # 만들 수 없는 경우 -1 출력