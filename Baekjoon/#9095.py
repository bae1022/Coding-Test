t = int(input()) # 테스트케이스의 개수

dp = [1, 2, 4]

for i in range(3, 11):
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

for i in range(t):
    n = int(input())

    print(dp[n - 1])