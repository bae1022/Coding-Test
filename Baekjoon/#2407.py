n, m = map(int, input().split())

dp = [0] * (m + 1)

cnt = m

dp[1] = n
for i in range(2, m + 1):
    n -= 1
    cnt = i

    dp[i] = dp[i - 1] * n // cnt

print(dp[m])