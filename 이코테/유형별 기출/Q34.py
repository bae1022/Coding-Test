n = int(input())

att = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if att[i] < att[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

