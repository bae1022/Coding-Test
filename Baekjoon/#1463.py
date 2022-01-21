n = int(input())

INF = 1e9
dp = [INF] * 1000001

dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

if n > 3:
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 2])

        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 3])

print(dp[n])