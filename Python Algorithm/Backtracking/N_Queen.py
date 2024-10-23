
# 아주 유명한 백트래킹 문제를 풀어보자.

'''
NxN 사이즈 체스판에 N개의 퀸 놓는 모든 경우의수 구하기

input = 4
output = 2
'''

# def queen(N):
# graph = [[0 for _ in range(N)] for _ in range(N)]

# 이전에 놓아진 queen 자리를 보고, 현재 row, col에 queen을 놓을 수 있는 자리인지 아닌지 판단하기.
def is_safe(queens, row, col):
    for r, c in enumerate(queens):
        # 같은 열에 queen이 이미 놓아졌으면 False, 지금까지 놓아진 queen들 대각선 체크
        if c == col or (abs(r-row) == abs(c-col)):
            return False
    return True

def solve(queens, row, N):
    if row == N:
        result.append(queens[:])
        return

    else:
        for col in range(N):
            if is_safe(queens, row, col):
                queens.append(col)
                solve(queens, row + 1, N)
                queens.pop()


result = []
solve(queens=[], row=0, N=5)

print(len(result))
print(result)