# ----- 6
# def findMinWeight(weights, d):
#     # Write your code here
#     import heapq, math
#     weights = [-w for w in weights]
#     heapq.heapify(weights)
    
#     for i in range(d):
#         largest = -heapq.heappop(weights)
#         heapq.heappush(weights, -math.ceil(largest/2))
#         print(weights, d)

#     return -sum(weights)
# weights = [30, 10, 25]
# d = 4

# print(findMinWeight(weights, d))

# ----- 5
# from collections import Counter

# def programmerStrings(s):
#     # Write your code here
    
#     search_word = 'programmer'
#     def find_idx(s, search_word):
#         word_counter = Counter(search_word)
#         s_counter = Counter()
#         idx = 0
#         while idx < len(s):
#             s_counter[s[idx]] += 1
            
#             if word_counter - s_counter == Counter():
#                 return idx
#             else:
#                 idx +=1
    
#     left_idx = find_idx(s, search_word)
#     right_idx = len(s) - find_idx(s[::-1], search_word)
    
#     return right_idx - left_idx - 2

# ---- 2
# def nodeDistance(s_nodes, s_from, s_to):
#     graph = [[] for _ in range(s_nodes+1)]
#     parent = [-1 for _ in range(s_nodes)]
#     visited = [False for _ in range(s_nodes)]
#     cycles = []
#     edges = zip(s_from, s_to)
    
#     for u, v in edges:
#         graph[u].append(v)
#         graph[v].append(u)
    
#     # use dfs
#     def find_cycle(node, parent):
#         visited[node] = True
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 parent[neighbor] = node
#                 if find_cycle(neighbor, node):
#                     True
                    
#             elif neighbor != parent:
#                 cycle = []
#                 current = node
#                 cycle.append(current)
#                 while current != neighbor:
#                     current = parent[current]
#                     cycle.append(current)
#                 cycles.append(cycle)
#                 return True
#         return False

#     for i in range(s_nodes):
#         if not visited[i]:
#             if find_cycle(i, -1):
#                 break
                
#     return cycles
    


# ---- 3
# 테스트케이스 11~14 타임익시드 에러.
# 이 부분 나중에 힙으로 다시 정리해보자.

from collections import deque
import heapq

def sumVips(score, guilder_count, k):
    # Write your code here
    score_queue = deque(score)
    selected_score = 0
    
    for _ in range(guilder_count):
        if len(score) < k:
            max_score = max(score_queue)
            selected_score += max_score
            score_queue.remove(max_score)
            
        else:
            front_slice = list(score_queue)[:k]
            back_slice = list(score_queue)[-k:]
            
            front_max = max(front_slice)
            back_max = max(back_slice)
            
            front_idx = score_queue.index(front_max)
            back_idx = len(score_queue) - k + back_slice.index(back_max)
            
            if front_max > back_max:
                selected_score += front_max
                del score_queue[front_idx]
            elif front_max < back_max:
                selected_score += back_max
                del score_queue[back_idx]
            else:
                selected_score += front_max
                del score_queue[front_idx]
                
    return selected_score
    