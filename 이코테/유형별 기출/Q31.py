t = int(input())

array = []
for _ in range(t):
    n, m = map(int, input().split()) # n * m
    array = list(map(int, input().split()))

    dp = []
    index = 0

    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for j in range(1, m): # 맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다.
        for i in range(n):
            if i == 0:
                left_up = 0 # 왼쪽 위에서 오는 경우는 없다.
            else:
                left_up = dp[i - 1][j - 1]

            if i == n - 1:
                left_down = 0 # 왼쪽 아래에서 오는 경우는 없다.

            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)