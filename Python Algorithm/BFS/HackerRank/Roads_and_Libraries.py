#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    visited = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
        
    # create cities graph
    for city in cities:
        s, e = city
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)
        
    # BFS
    def bfs(graph, start, visited):
        from collections import deque
        queue = deque([start])
        visited[start] = 1
        size = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = 1
                    size += 1
        return size

    
    def find_island_size(graph):
        is_island_count = 0
        island_sizes = []
        
        for node in range(len(graph)):
            if not visited[node]:
                size = bfs(graph, node, visited)
                island_sizes.append(size)
                is_island_count += 1
        return island_sizes
        
    island_sizes = find_island_size(graph)
    
    total_cost = 0
    for island in island_sizes:
        if c_lib <= c_road:
            cost = c_lib * island
        else:
            cost = c_lib + (island-1) * c_road
        total_cost += cost
    
    return total_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
