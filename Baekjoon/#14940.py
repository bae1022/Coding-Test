from collections import deque

n, m = map(int, input().split())

field = [[-1] * m for _ in range(n)]

for i in range(n):
    col = list(map(int, input().split()))

    for j in range(m):
        if col[j] == 2:
            start = ((i, j))

        elif col[j] == 1:
            field[i][j] = -1

        elif col[j] == 0:
            field[i][j] = 0

visited = [[False] * m for _ in range(n)]
field[start[0]][start[1]] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))

    visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()

        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == -1:
                if not visited[nx][ny]:
                    field[nx][ny] = cnt + 1

                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True

bfs(start[0], start[1])

for i in range(n):
    for j in range(m):
        print(field[i][j], end=' ')

    print()