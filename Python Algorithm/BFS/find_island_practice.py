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

from collections import deque

def bfs(graph, start):
    global island_cnt
    queue = deque([start])
    
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[ny][nx] and graph[ny][nx] == 1:
                        queue.append([ny, nx])
    else:
        island_cnt += 1

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1 and not visited[y][x]:
            bfs(graph, [y, x])

result = island_cnt