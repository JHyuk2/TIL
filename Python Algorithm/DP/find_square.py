'''
가장 큰 정사각형 찾기

5 5
1 1 1 0 0
1 1 1 1 0
1 1 1 1 0
0 1 1 1 0
0 0 1 1 1

출력
3
'''

n, m = map(int, input().split())

graph = []
dp = [[0 for _ in range(m)] for _ in range(n)]
for y in range(n):
    graph.append(list(map(int, input().split())))

result = 0
# for y in range(n):
#     for x in range(m):
#         if x-1>=0 and y-1>=0:
#             dp[y][x] = min(dp[y][x], dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1
#         else:
#             dp[y][x] = graph[y][x]
    
#         if dp[y][x] >= result:
#             result = dp[y][x]

for y in range(n):
    for x in range(m):
        if x>0 and y>0 and graph[y][x] == 1:
            dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1
        else:
            dp[y][x] = graph[y][x]
    
        if dp[y][x] >= result:
            result = max(dp[y][x], result)