from collections import deque

def solution(edges):
    # 1. 먼저 생성된 노드를 찾기.
    # 생성된 노드는 "자기 자신으로 들어오는 간선은 0, 내보내는 간선은 2개 이상"
    # 내보내는 간선이 2개 이상이면 생성된 노드로 확정 가능(그래프의 수의 합은 2 이상이기 때문)
    # 찾는 것은 예외처리 없이 적용 가능
    
    # 딕셔너리를 사용하는 게 좋아보임.
    graphs = dict()
    for edge in edges:
        start, end = edge
        try:
            graphs[start].append(end)
        except:
            graphs[start] = [end]

    flattened = []
    temp_8 = []
    for key, value in graphs.items():
        if len(value) == 2:
            temp_8.append(key)
        flattened += value

    # 들어오는 간선이 있는 모든 애들은 flattened에 속함.
    # 만약 flattened에 없는 노드가 1개 뿐인 경우, 생성된 노드임.
    # 만약 flattened에 없는 노드가 2개 이상인 경우, 내보내는 간선 갯수를 확인해야함.
    flattened = set(flattened)
    node_num = max(max(graphs.keys()), max(flattened))
    temp_set = {i+1 for i in range(node_num)}
    
    # 노드 체크
    node_check = temp_set - flattened
    for check in node_check:
        # 길이가 1인 경우,
        if len(node_check) == 1:
            created_node = check
            break
        # 길이가 2이상인 경우,
        else:
            # 내보내는 간선이 있는 경우
            try:
                temp = graphs[check]
                # 2개 이상 내보내면 created_node 확정
                if len(temp) >= 2:
                    created_node = check
            # 내보내는 간선이 없는 경우는 생각 안해도 됨.
            except:
                continue
    
    # 생성된 정점
    print(created_node)
        
    # 2. 생성된 노드의 모든 연결을 끊고 모든 노드 일단 표시
    del graphs[created_node]
    temp_list = [i+1 for i in range(node_num)]
    temp_list.remove(created_node)
    
    # 모든 노드를 방문해야함.
    visited = [0 for _ in range(node_num+1)]
    visited[created_node] = 1

    # 3. 나뉘어진 각 그래프가 어떤 모양인지 체크!
    # 3-1) 가장 먼저, 8자 모양 그래프가 있는지를 찾기
    # 8자 모양 그래프가 있는 경우, graphs.values에서 길이가 2인 노드가 반드시 존재함.
    # 그러면, 그것과 이어진 모든 노드를 8자 그래프로 떼어내 줄 수 있음.
    graph_8_node = [i for i in temp_8 if i != created_node]
    
    # 8자 그래프가 있는 경우, 모든 노드 찾아서 제거해주기.
    if graph_8_node:
        for cur in graph_8_node:
            queue = deque(graphs[cur])
            
            while queue:
                next_node = queue.popleft()
                if visited[next_node]:
                    continue
                else:
                    queue += graphs[next_node]
                    del graphs[next_node]
                    visited[next_node] = 1

    print(graphs, visited)
    # 막대 개수는 대충 알 수 있음.
    stick = (node_num - sum(visited)) - len(graphs.keys())
    donut = 0
    
    # 3-2) 남은 친구들을 막대와 도넛으로 구분하기.
    if graphs:
        for k, v in graphs.items():
            if visited[k]:
                continue
            else:
                queue = deque(v)
                while queue:
                    cur_node = queue.popleft()
                    if visited[cur_node]:
                        donut += 1
                        break
                    else:
                        visited[cur_node] = 1
                        try:
                            temp = graphs[cur_node]
                            queue.append(temp[0])
                        except:
                            continue

    answer = [created_node, donut, stick, len(graph_8_node)]
    return answer