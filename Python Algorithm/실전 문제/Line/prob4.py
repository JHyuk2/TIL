def solution(snapshots, transactions):
    # 1) snapshot 계좌와 금액을 각각 str:int 쌍의 딕셔너리로 생성
    snap_dict = {}
    for s in snapshots:
        snap_dict[s[0]] = int(s[1])
    # 2) 모든 트랜잭션을 돌면서 금액 더해주기
    used_id = []
    for t in transactions:
        ID2 = t[0]
        # 2-1) 이미 했던 트랜잭션은 넘어가자!
        if ID2 in used_id:
            continue
        # 잔액이 음수가 되는 트랜잭션은 없으니, 없을 때 + 인 경우만 생각해주면 된다.
        else:
            used_id.append(ID2)
            if t[1] == 'SAVE':
                # 없는 경우에만 추가
                if t[2] not in snap_dict.keys():
                    snap_dict[t[2]] = int(t[3])
                else:
                    snap_dict[t[2]] += int(t[3])
            # t[1] == "WITHDRAW"
            else:
                snap_dict[t[2]] -= int(t[3])  
        
    answer = []
    for acc, money in snap_dict.items():
        answer.append([acc, str(money)])
    return sorted(answer, key = (lambda x :x[0]))