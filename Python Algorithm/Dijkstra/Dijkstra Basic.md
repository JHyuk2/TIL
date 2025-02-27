# 다익스트라 알고리즘

다익스트라(Dijkstra) 알고리즘은, 여러 길이 있을 때 한 곳에서 다른 곳까지 가는 `가장 빠른 길을 찾는 방법`이다.

BFS, DFS와는 다르게 힙큐(우선순위 큐, Heap Queue)를 사용하는 알고리즘.



### 힙큐(Heap Queue)를 왜 쓸까?

힙큐는 **우선순위가 높은 것부터 빠르게 처리**하는 도구로, 다익스트라에서는 제일 빠른 길을 먼저 확인하고, 그 길로 먼저 가보는 방법을 사용한다.

#### 만약 BFS와 DP로 구현하면 어떻게 될까?

- **BFS (너비 우선 탐색)** : BFS는 한 번에 한 단계씩 모든 길을 동시에 살펴보는 방법으로, 모든 갈림길을 다 한번에 본다고 생각하면 된다. 만약 거리가 같은 길을 찾을 땐 괜찮지만, 가장 빠른 길을 찾는 문제에서는 비효율적이다. 왜냐면, BFS는 힙큐처럼 "더 빠른 길"을 우선적으로 보는 게 아니라, 모든 갈림길을 한 번씩 가보고 판단하기 때문에, 그래프가 커지고 복잡해질수록 불필요한 계산량이 늘어나게 된다.
- **DP (동적 계획법)** : DP는 복잡한 문제를 여러 개의 문제로 나누어 해결하는 방법이다. 만약 한 번 계산한 길에 대한 정보를 잘 저장한다면, 나중에 또 같은 길을 계산할 필요가 없게 만드는 방법인데, 다익스트라는 길을 하나하나 확인하면서 길을 찾아야 하기 때문에, DP는 다익스트라가 필요한 상황에선 잘 맞지 않을 수 있다. >> 길의 "우선순위"를 실시간으로 결정하기가 어렵기 때문



