'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''

from collections import deque

N, M ,V = map(int, input().split()) # Node, Edge, Root
adj_graph = {n+1:[] for n in range(N)}

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue += graph[node ]-set(visited)
    return visited
        
# 1. 그래프 입력
for _ in range(M):
    s, e = map(int, input().split())
    adj_graph[s].append(e)
    adj_graph[e].append(s)

keys = adj_graph.keys()
for k in keys:
    adj_graph[k] = set(adj_graph[k])


result = bfs(adj_graph, V)
print(result)

def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node])-set(visited))
                temp.sort(reverse=True)
                stack+=temp
    return " ".join(str(i) for i in visited)

dfs_result = dfs(adj_graph, V)
print(dfs_result)