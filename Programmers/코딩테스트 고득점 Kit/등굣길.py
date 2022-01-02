def solution(m, n, puddles):
    answer = 0

    dp = [[0] * m for _ in range(n)]

    for i in range(len(puddles)):
        y, x = puddles[i]

        dp[x - 1][y - 1] = -1

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue

            if dp[i][j] == -1:
                continue

            elif i - 1 < 0:
                dp[i][j] = dp[i][j - 1]

            elif j - 1 < 0:
                dp[i][j] = dp[i - 1][j]

            else:
                if dp[i - 1][j] == -1:
                    dp[i][j] = dp[i][j - 1]

                elif dp[i][j - 1] == -1:
                    dp[i][j] = dp[i - 1][j]

                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    if dp[n - 1][m - 1] != -1:
        answer = dp[n - 1][m - 1]

    else:
        answer = 0

    return answer % 1000000007

print(solution(4, 3, [[2, 2]])) # 4
print(solution(4, 3, [[2, 1], [1, 2]]))