n, m = map(int, input().split())

field = [[0] * n for _ in range(n)]
for i in range(n):
    col = list(map(int, input().split()))
    for j in range(n):
        field[i][j] = col[j]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

rain = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]

for _ in range(m):
    d, s = map(int, input().split())

    visited = [[False] * n for _ in range(n)]
    next_rain = []

    for i in range(len(rain)): # 비구름이 옮겨가고, 비가 내린다.
        x, y = rain[i]

        rain[i][0], rain[i][1] = (x + dx[d - 1] * s) % n, (y + dy[d - 1] * s) % n

        next_rain.append([rain[i][0], rain[i][1]])

    for i in range(len(next_rain)):
        x, y = next_rain[i]

        field[x][y] += 1
        visited[x][y] = True

    rain = []

    rx = [-1, -1, 1, 1]
    ry = [-1, 1, -1, 1]

    for i in range(len(next_rain)):
        x, y = next_rain[i]

        cnt = 0
        for j in range(4):
            if 0 <= x + rx[j] < n and 0 <= y + ry[j] < n:
                if field[x + rx[j]][y + ry[j]] != 0:
                    cnt += 1

        field[x][y] += cnt

    # 구름이 다시 생성
    for i in range(n):
        for j in range(n):
            if field[i][j] >= 2 and visited[i][j] is False:
                field[i][j] -= 2
                rain.append([i, j])

answer = 0
for i in range(n):
    for j in range(n):
        answer += field[i][j]

print(answer)