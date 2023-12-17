from itertools import combinations, product

# 조합 때려박으면 되는건가..?
def solution(dice):
    # 주사위를 챙길 수 있는 가지수
    dice_num = [i for i in range(len(dice))]
    combi = list(combinations(dice_num, len(dice_num)//2))
    mid = len(combi) // 2
    max_diff = 0
    
    for i in range(mid):
        team_A = combi[i]
        team_B = combi[-i-1]
        # 모든 경우의 수 찾기.
        # 먼저 A팀 주사위로 나올 수 있는 모든 경우의 수
        A_dice = []
        B_dice = []
        for num in team_A:
            A_dice.append(dice[num])
        for num in team_B:
            B_dice.append(dice[num])

        A_product = product(*A_dice)
        A_product = map(sum, A_product)
        B_product = product(*B_dice)
        B_product = map(sum, B_product)
        res = product(A_product, B_product)
        res = list(map(lambda x:1 if x[0]-x[1]>0 else 0 if x[0]==x[1] else -1, res))

        diff = res.count(1) - res.count(-1)

        if max_diff < abs(diff):
            max_diff = abs(diff)
            
            # A의 승이 더 많은 경우
            if diff > 0:
                answer = team_A
            else:
                answer = team_B
    answer = list(sorted(map(lambda x:x+1, answer)))
    return answer