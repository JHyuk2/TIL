'''
입력값

5 6
1 0 1 1 1 1
1 0 1 0 1 0
1 0 1 0 1 1
1 1 1 0 1 1
0 0 0 0 1 1

출발: (0, 0)
도착: (4, 5)

도착 지점까지 걸리는 거리 구하기.

출력값 : 15

'''
# from sys import stdin
# input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)


# left, up, right, down
dx = [ -1, 0, 1, 0]
dy = [0, 1, 0, -1]

from collections import deque
def bfs(graph, start):
    queue = deque([(start, 1)])
    visited = [[0 for _ in range(m)] for _ in range(n)]

    while queue:
        (y, x), size = queue.popleft()
        
        if y == n - 1 and x == m - 1:
            return size

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 범위를 벗어나지 않고, 길이 있는 경우에만
            if (0 <= next_x < m) and (0 <= next_y < n) and (graph[next_x][next_y]==1):
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = size
                    queue.append([(next_x, next_y), size+1])
                # else:
                #     if visited[next_x][next_y] < size:
                #         visited[next_x][next_y] = size
    return size

result = bfs(graph, start=(0, 0))
print(result)