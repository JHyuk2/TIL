# # 문제 1)
from collections import deque
a = 0
queue = deque()

while a != '-1':
    a = input("양의 정수를 입력하세요(종료: -1) : ")
    queue.append(a)
res = ''
for q in queue:
    if q == '-1':
        res += 'None'
    else:
        res += q + '->'
print(res)

# 문제 2~5) 연결리스트 class 작성

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    num_of_elems = 0
    def __init__(self):
        self.head = None
        self.tail = None
    
    # 삽입
    def add_node(self, item):
        new_node = Node(item)
        # 비어있지 않으면
        if self.num_of_elems:
            # 길이가 2 이상인 경우
            if self.head.link:
                self.tail.link = new_node
                self.tail = new_node    
                self.num_of_elems += 1
            # 현재 길이가 1인 경우
            else:
                self.head.link = new_node
                self.tail = new_node
                self.num_of_elems += 1
        # 비어있으면    
        else:
            self.head = new_node
            self.tail = new_node
            self.num_of_elems += 1 
    # 삭제
    def pop_node(self):
        if self.num_of_elems:
            cur = self.head
            if self.num_of_elems == 1:
                self.num_of_elems -= 1
                self.head = None
                self.tail = None
                return cur.data
            
            for i in range(num_of_elems-2):
                cur = cur.link
            else:
                tmp = cur.link
                cur.tail = None
                self.num_of_elems -=1
                return tmp.data
        else:
            return None

    # 헤드, 테일, 원소갯수, 비어있는지
    def get_head(self):
        return self.head.data
    def get_tail(self):
        return self.tail.data
    def get_num_of_elems(self):
        return self.num_of_elems
    def isEmpty(self):
        return False if self.num_of_elems else True

    # 전체 출력
    def display(self):
        cur = self.head
        res = ''
        while cur.link:
            res += str(cur.data) + '->'
            cur = cur.link
        res += str(cur.data) + '->'
        return res
    
    def del_head(self):
        self.head = self.head.link
        self.num_of_elems -= 1
        
    def get_data_sum(self):
        tmp_sum = 0
        cur = self.head
        while cur.link:
            tmp_sum += cur.data
            cur = cur.link
        tmp_sum += cur.data
        return tmp_sum

    def count_node(self, elem):
        cnt = 0
        cur = self.head
        while cur.link:
            if elem == cur.data:
                cnt += 1
            cur = cur.link

        if elem == cur.data:
            cnt += 1
        return cnt

# 실행문
LL = LinkedList()
for i in range(int(input("노드의 개수 :"))):
    a = int(input(f"노드 #{i+1} 데이터 :"))
    LL.add_node(a)
print(f'생성된 연결 리스트 : {LL.display()}')

print('-----------------------------------------')
# # 문제 3) 연결 리스트의 맨 처음에 있는 노드를 삭제하는 프로그램 작성하기.
LL = LinkedList()
for i in range(int(input("노드의 개수 :"))):
    a = int(input(f"노드 #{i+1} 데이터 :"))
    LL.add_node(a)
print(f'생성된 연결 리스트 : {LL.display()}')
LL.del_head()
print(f'첫 번째 노드 삭제 후 연결 리스트 : {LL.display()}')

print('-----------------------------------------')
# 문제 4) 연결 리스트 데이터 합
LL = LinkedList()
for i in range(int(input("노드의 개수 :"))):
    a = int(input(f"노드 #{i+1} 데이터 :"))
    LL.add_node(a)
print(f'연결 리스트의 데이터 합: {LL.get_data_sum()}')

print('-----------------------------------------')

# 문제 5) 노드의 개수 계산
LL = LinkedList()
for i in range(int(input("노드의 개수 :"))):
    a = int(input(f"노드 #{i+1} 데이터 :"))
    LL.add_node(a)
find_num = int(input("탐색할 값을 입력하시오: "))
print(f'{ find_num }는 연결 리스트에서 {LL.count_node(find_num) }번 나타납니다.')