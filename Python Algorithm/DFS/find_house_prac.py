'''
인접한 단지의 갯수찾기
+ 각 단지마다 얼마나 붙어있는지 출력하기

입력
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

출력

3
7
8
9
'''

n = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    temp = input()
    for s in temp:
        graph[i].append(int(s))

# n x n 
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


cnt_list = []
def dfs(y, x):
    visited[y][x] = True
    global cnt
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < n and graph[ny][nx]==1 and not visited[ny][nx]:
            dfs(ny, nx)


total_house = 0
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            cnt = 0
            dfs(y, x)
            total_house += 1
            cnt_list.append(cnt)

print(total_house)
for i in range(len(cnt_list)):
    print(cnt_list[i])
