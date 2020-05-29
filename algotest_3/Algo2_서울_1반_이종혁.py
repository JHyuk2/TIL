from itertools import permutations

for tc in range(int(input())):
    N, M = map(int, input().split())
    # 사탕 개수는 필요 없는 정보다.
    candy_in_children = [set(list(map(int, input().split()))[1:]) for _ in range(N)] 

    # 학생이든 캔디든 적은 쪽을 기준으로 반복 실행
    tmp = min(N, M)
    permute = list(permutations([i+1 for i in range(M)], tmp))
    
    # tmp횟수 중 변화가 일어나는 카운트해서 res에 더해주면 된다.
    min_passed = 10
    tmp_result = sum(map(len, candy_in_children))

    for p in range(len(permute)):
        cur_passed = 0
        tmp_permute = permute[p]
        for i in range(tmp):
            if tmp_permute[i] in candy_in_children[i]:
                cur_passed += 1
                # 현재까지 지나친 횟수가 이미 min_passed가 된 경우, 더이상 진행할 필요가 없다.
                if cur_passed >= min_passed:
                    break
        # for else
        else:    
            min_passed = cur_passed
    
    # min_passed를 찾았다면, (전체 try - 지나친 경우) 를 더해주면 된다.
    tmp_result += tmp - min_passed
    print(f'#{ tc+1 } { tmp_result }')