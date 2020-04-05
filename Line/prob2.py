def solution(answer_sheet, sheets):
    length = len(sheets)
    answer = 0
    scores = []
    # 1) 두 개의 답안을 모두 뽑음
    for i in range(length):
        for j in range(i+1, length):
            max_doubt = 0
            doubt = 0
            cnt = 0
            # 2) 뽑힌 두 개를 비교하여 의심문항, 가장 긴 연속된 의심 문항 수 출력
            s1 = sheets[i]
            s2 = sheets[j]
            for idx in range(len(answer_sheet)):
                if s1[idx] == s2[idx] and s1[idx] != answer_sheet[idx]:
                    doubt += 1
                    cnt +=1
                else:
                    if cnt:
                        if max_doubt < cnt:
                            max_doubt = cnt
                        cnt = 0
            else:
                if cnt:
                    if not max_doubt:
                        max_doubt = cnt
            scores.append(doubt + (max_doubt)**2)
            
    answer = max(scores)
    return answer