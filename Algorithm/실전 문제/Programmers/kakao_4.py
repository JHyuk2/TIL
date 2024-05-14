# 점화식과 계차수열
def solution(n, tops):
    dp = [0] + [0 for _ in range(n+1)]
    dp[1] = 3
    for i in range(2, n+2):
        j = (i-1)*2
        temp_sum = j*(j+1) //2
        dp[i] = dp[i-1] + 2 + temp_sum
        print(dp)
    answer = 0
    return answer

    # [0, 1, 3, 8, 20, 43]