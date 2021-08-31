# 예제 4
# 금광_ n * m 크기의 금광이 있고, 각 칸에 특정한 크기의 금이 있다. m - 1에 걸쳐서 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다. 채굴자가 어등ㄹ 수 있는 금의 최대 크기는?
# +) 시작은 첫번째 열이며, 행은 선택할 수 있다.

# 점화식 dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1]
#                   현재위치               왼쪽위            왼쪽             왼쪽 아래

num = int(input()) # 테스트 케이스 개수

for tc in range(num):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0

    for i in range(n):
        dp.append(array[index:index + m]) # 금광 정보가 한 줄에 쭉 이어지기 때문에 슬라이싱 작업
        index += m

    for j in range(1, m): # 각 열마다 전체 행 확인함
        for i in range(n):

            # 왼쪽 위에서 오는 경우
            if i == 0: # 경로 벗어나는 경우
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽 아래에서 오는 경우
            if i == n - 1: # 경로 벗어나는 경우
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0

    for i in range(n):
        result = max(result, dp[i][m - 1]) # 가장 오른쪽 열에 있는 값 중 가장 큰 값을 선택

    print(result)