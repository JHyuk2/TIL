# 주사위를 세 번 굴린다.
# (score, tempt, wins)
# score가 6일 때 win일 확률 구하기.
result_list = [(2, 1, 1), (4, 1, 1), (6, 1, 1)]

# 만약 score가 6이 나오면서 tempt와 wins가 같은 경우, 정답이라고 볼 수 있다.
tempt_cnt = 0
wins_cnt = 0
total_score = 6 # target score

while result_list : 
    print(result_list)
    cur_score, cur_tempt, cur_wins = result_list.pop()
    if cur_tempt == 3:
        if cur_score == 6:
            tempt_cnt += 1
            if cur_wins == 3:
                wins_cnt += 1
        continue

    for i in range(1, total_score - cur_score + 1):
        if i % 2 :
            score = 0
            tempt = 1
            wins = 0
        else:
            score = i
            tempt = 1
            wins = 1

        result_list.append((cur_score + score, cur_tempt + tempt, cur_wins + wins))

print(tempt_cnt, wins_cnt)