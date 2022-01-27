n, m = map(int, input().split())

field = [[0] * m for _ in range(n)]

for i in range(n):
    col = list(map(int, input().split()))

    for j in range(m):
        field[i][j] = col[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_temp = 0
visit = [[False] * m for _ in range(n)]

def dfs(x, y, depth, temp): # ㅏ 모양 제외 할 수 있는 모양들을 모두 측정
    global max_temp

    if depth == 3:
        if temp > max_temp:
            max_temp = temp
        return

    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    dfs(nx, ny, depth + 1, temp + field[nx][ny])
                    visit[nx][ny] = False

def shape(x, y):
    center = field[x][y]

    limit = 4

    min_shape = 100000
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if limit <= 2:
            return 0 # 모양을 생성할 수 없음

        if 0 <= nx < n and 0 <= ny < m:
            center += field[nx][ny]

            if min_shape > field[nx][ny]:
                min_shape = field[nx][ny]

        else:
            limit -= 1

    if limit == 4:
        center -= min_shape

    return center

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i, j, 0, field[i][j])
        visit[i][j] = False

        temp = shape(i, j)

        if temp > max_temp:
            max_temp = temp

print(max_temp)