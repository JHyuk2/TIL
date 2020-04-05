def solution(dataSource, tags):
    count_list = [0 for _ in range(len(dataSource))]
    answer = []
    for idx, data in enumerate(dataSource):
        count = 0
        d_tag = data[1:]
        for d in d_tag:
            if d in tags:
                count +=1
            if len(tags) == count:
                count_list[idx] = count
                continue
        else:
            count_list[idx] = count
    
    # 결과값 받기
    for i in range(len(count_list)):
        tmp_max = max(count_list)
        # 하나 이상 동일한 태그를 가져야 함.
        if not tmp_max :
            break
        cnt = count_list.count(tmp_max)
        for _ in range(cnt):
            idx = count_list.index(tmp_max)
            answer.append(dataSource[idx][0])
            count_list[idx] = 0
        # 상위 10개만 출력
        if len(answer) >= 10:
            answer = answer[:10]
            break
    return answer