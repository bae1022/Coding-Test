n, k = map(int, input().split()) # n 종류의 동전, k원이 되게 하고 싶다.

coins = []

for _ in range(n):
    coins.append(int(input()))

result = 0

dp = [0] * (k + 1)
dp[0] = 1

for i in coins:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])