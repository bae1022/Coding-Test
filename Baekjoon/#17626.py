import math

n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(1, n + 1):
    x = math.sqrt(i)

    if x % 1 == 0: # 제곱수라면
        dp[i] = 1

    else: # 제곱수가 아니라면
        dp[i] = i

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[j * j] + dp[i - (j * j)])

print(dp[n])

