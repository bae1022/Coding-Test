n, k = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())

    coins.append(coin)

dp = [10001] * (k + 1) # 금액을 만들어내는 데 필요한 최소 동전 개수

dp[0] = 0

for i in range(n):
    for j in range(coins[i], k + 1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[k] != 10001:
    print(dp[k])

else:
    print(-1)

