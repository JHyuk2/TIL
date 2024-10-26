'''

섬의 갯수 찾기

5 4
1 0 0 1 1
1 0 0 1 0
0 0 0 0 1
0 1 1 0 0

출력  4
'''

m, n = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]

graph = []
for _ in range(4):
    graph.append(list(map(int, input().split())))

# left, up, right, down
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

island_cnt = 0

def dfs(node):
    y, x = node
    if not visited[y][x]:
        visited[y][x] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    dfs([ny, nx])

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1 and not visited[y][x]:
            dfs([y, x])
            island_cnt += 1

result = island_cnt