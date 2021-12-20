def solution(n):
    answer = 0

    dp = [-1] * 60001

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    answer = dp[n]

    return answer

print(solution(4)) # 5