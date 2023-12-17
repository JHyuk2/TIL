N = int(input())
maps = []

# maps, get start position
for i in range(N):
    current_line = list(map(int, input().split()))
    maps.append(current_line)
    if 9 in current_line:
        start_x = current_line.index(9)
        start_y = i
        pos = (start_y, start_x)

# size == count 가 되는 순간, size += 1, count=0
size = 2
count = 0 

# 자신보다 작은 물고기만 먹을 수 있고,
# 자신보다 큰 물고기는 지나갈 수 없음
# 자신의 몸집 사이즈만큼 먹으면 사이즈가 1 커짐
# 먹을 수 있는 물고기가 1마리보다 많으면 가장 가까운 물고기(BFS)
# 가까운 물고기가 많다면 가장 위에 있는 가장 왼쪽의 물고기

# 1) 먹을 수 있는 물고기 찾기(BFS)
# 1-1) BFS로 자신보다 작은 물고기들을 찾고, 거리와 함께 등록
# 1-2) 

# 북 서 남 동 순서로 할거임
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


from collections import deque
queue = deque(pos)
def bfs(queue):
    global N
    global size
    global count    

    visited = [[0]*N for _ in range(N)]
    while queue:
        temp = queue.popleft()
        y = temp[0]
        x = temp[1]
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 먼저 이동할 수 있는 곳이어야 함.
            if (0 <= nx < N) or (0 <= ny < N):
                if maps[ny][nx] <= size:



def find_fishes(maps, current_pos):
    eatable = []
    y = current_pos[0]
    x = current_pos[1]
    
    return
# 2) 