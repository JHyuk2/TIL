def solution(inputString):
    opener = ['(', '{', '[', '<']
    closer = [')', '}', ']', '>']
    stack = []
    res = 0
    for s in inputString:
        if s in opener:
            stack.append(s)
        if s in closer:
            # 비정상 케이스
            if not stack:
                return -1
            # stack이 들어있는 경우
            else:
                tmp = stack.pop()
                if opener[closer.index(s)] == tmp:
                    res += 1
                    continue
                else:
                    return -1
    return res