def solution(road, n):
    # 연속된 부분을 보수할 수 있다.
    # 1) 1인 부분과 0인 부분을 나눈다.
    one_tmp = ''
    zero_tmp = ''
    road_split = []
    
    for idx, s in enumerate(road):
        if s == '1':
            one_tmp += s
            if zero_tmp:
                road_split.append(zero_tmp)
                zero_tmp = ''
        if s == '0':
            zero_tmp += s
            if one_tmp:
                road_split.append(one_tmp)
                one_tmp = ''
    else:
        if one_tmp:
            road_split.append(one_tmp)
        else:
            road_split.append(zero_tmp)
    # 일단 다 쪼개지긴 했음
    # 2) 모든 경우의수에 따라 길을 고름
    answer = 0
    for i in range(len(road_split)):
        for j in range(i+1, len(road_split)+1):
            remain = n
            tmp_road = road_split[i:j]
            length = 0
            for k in tmp_road:
                if k[0] == '1':
                    length += len(k)
                if k[0] == '0':
                    if remain >= len(k):
                        remain -= len(k)
                        length += len(k)
                    else:
                        if answer < length:
                            answer = length
                        break
            # for else // 끝까지 간 경우
            else:
                if answer < length:
                    answer = length
    return answer