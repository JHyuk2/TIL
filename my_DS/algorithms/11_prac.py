import heapq as hq


q = []
f = True
while True:
    f = input("삽입(i), 삭제(d): ")
    if f == 'i':
        todo = input("할 일: ")
        p = int(input("우선순위: "))
        hq.heappush(q, (p, todo))
    
    elif f == 'd':
        p, todo = hq._heapify_max(q)
        
        print(f'제일 우선순위가 높은 일은 "{todo}"')
    
    else:
        print("메뉴선택 다시 하세요")
    
    print()