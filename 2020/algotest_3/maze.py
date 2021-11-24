# 방 데이터는 rooms 로 정의한다.

# 1) 나올 수 있는 출발지점들의 조합을 구한다.
# # - 모든 방 중 번호가 2인 방들을 리스트로 뽑고, combination 2로 추출.

from itertools import combinations
start_points = []

N = int(input())
rooms = 
# 1-1) 시작지점 구하기
for i in range(N):
    for j in range(N):
        if rooms[i][j] == 2:
            start_points.append((i, j))

# 1-2) 출발지점들의 조합 추출
combis = list(combinations(start_points, 2))

###
# 2) 위에서 구한 출발지점들의 조합들로부터 최단경로를 구한다.(bfs)

# 2-1) visited, 방향 설정 & bfs 구상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

from collections import deque

result = []

# 경로와 같이 result에 넣어줄 수 있는 bfs를 만든다.
def bfs(start, goal):
    queue = deque( [ (start, [start]) ] )

    while queue:
        cur, path = queue.popleft()
        if cur == goal:
            result.append(path)
            break
        else:
	        adj_list = []
            for i in range(4):
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]
	    if 0<= nx < N and 0 <= ny < N:
	        adj_list.append([nx, ny])

	# 중복되는 경로가 생기지 않게 조정(path == visited)
	for p in (adj_list - set(path)):
	    queue.append( (p, path + [p]) )

# 3) 이제 출발지점들로부터 돌아가며 bfs를 실행한다.
for c in combis:
    start = c[0]
    goal = c[1]
    bfs(start, goal)

# 4) result에 들어가 있는 것들 중, 가장 길이가 짧은 것을 찾아서 거리를 구해준다.

# 4-1) 두 지점의 최단 거리
shortest_length = min(list(map(len, result)))

# 4-2) 최단 시간 - 양쪽에서 진행할 수 있기 때문에 아래와 같이 시간을 구해준다.
shotest_time = (shortest_length+1) // 2

# [결과출력]
print(shortest_time)