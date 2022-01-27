n = int(input())

dp = [''] * (n + 1)
dp[1] = 'SK' # 상근이

for i in range(1, n + 1):
    if dp[i] != '':
        continue

    else:
        if dp[i - 1] == 'SK':
            dp[i] = 'CY'

        elif dp[i - 1] == 'CY':
            dp[i] = 'SK'

        elif dp[i - 3] == 'SK':
            dp[i] = 'CY'

        elif dp[i - 3] == 'CY':
            dp[i] = 'SK'

print(dp[n])