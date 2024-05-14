"""
["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
"""

# 브루트 포스 + 2차원 리스트
def solution(friends, gifts):
    # 1) 선물 지수 표 만들기
    present_list = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for gift in gifts:
        gived, received = gift.split()
        present_list[friends.index(gived)][friends.index(received)] += 1

    # 준 선물
    give_total = list(map(sum, present_list))
    # 받은 선물
    receive_total = list(map(sum, zip(*present_list)))
    # 선물 지수
    present_scope = list(map(lambda x:x[0] - x[1], zip(give_total, receive_total)))

    # 2) 받는 선물 계산하기.
    # 2-1) 자기 자신의 인덱스는 제외
    # 2-2) 준 선물 > 받은 선물인 경우 한 개 받기
    # 2-3) 주고받은 선물의 수가 같다면 선물지수 비교하기
    count_list = [0 for _ in range(len(friends))]
    
    for i in range(len(friends)):
        count = 0
        for j in range(len(friends)):
            # 본인 인덱스인 경우 넘어가기
            if i == j:
                continue
            # 준 선물이 많으면 count +=1
            if present_list[i][j] > present_list[j][i]:
                count += 1
            # 주고 받은 선물의 개수가 같으면 선물지수 비교하기
            elif present_list[i][j] == present_list[j][i]:
                if present_scope[i] > present_scope[j]:
                    count += 1
        # 선물 값 입력하기
        count_list[i] = count

    print(count_list)
    answer = 0
    return answer