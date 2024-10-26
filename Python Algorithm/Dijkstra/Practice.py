'''
도시 A, B, C, D, E가 있고, 각 도시 사이에 아래와 같은 길이 있다.

A -> B (5분)
A -> C (2분)
B -> D (4분)
C -> B (8분)
C -> D (7분)
D -> E (1분)
'''

import heapq
import sys

# 딕셔너리로 만들어야 조금 더 직관적으로 사용됨.
# input = sys.stdin.read().strip().splitlines()
graph = {}
with open('input.txt', 'r') as input:
    for line in input:
        node1, node2, time = line.split()
        time = int(time)
        if node1 not in graph:
            graph[node1] = {}
        graph[node1][node2] = time

def add_missing_nodes(graph):
    nodes = set(graph.keys())
    for node in graph:
        for neighbor in graph[node]:
            nodes.add(neighbor)

    for node in nodes:
        if node not in graph:
            graph[node] = {}


def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0 # 시작점은 거리가 0
    
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    while priority_queue:
        time, node = heapq.heappop(priority_queue)

        for neighbor in graph[node]:
            new_time = time + graph[node][neighbor]
            if new_time < distance[neighbor]:
                distance[neighbor] = new_time
                heapq.heappush(priority_queue, [new_time, neighbor])
    
    for node, dist in distance.items():
        print(f"{start}에서 {node}까지의 최단 경로는 {dist}입니다.")
    
add_missing_nodes(graph)
dijkstra(graph, 'A')
