def solution(n):
    answer = 0

    dp = [-1] * 100001

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    answer = dp[n] % 1234567

    return answer

print(solution(3)) # 2
print(solution(5)) # 5