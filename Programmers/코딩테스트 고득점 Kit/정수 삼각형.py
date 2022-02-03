import copy


def solution(triangle):
    dp = copy.deepcopy(triangle)

    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], triangle[i + 1][j] + dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], triangle[i + 1][j + 1] + dp[i][j])

    answer = max(dp[len(triangle) - 1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))