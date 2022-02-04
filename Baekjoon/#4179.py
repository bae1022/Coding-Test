from collections import deque

n, m = map(int, input().split())
field = [[''] * m for _ in range(n)]

jh = deque()
fire = deque()

for i in range(n):
    col = input()

    for j in range(m):
        field[i][j] = col[j]

        if col[j] == 'J':
            jh.append((i, j))

        if col[j] == 'F':
            fire.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
found = False

visited = [[False] * m for _ in range(n)]
f = [[False] * m for _ in range(n)]
while jh:
    time += 1

    for _ in range(len(fire)):
        x, y = fire.popleft()
        f[x][y] = True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] != '#' and f[nx][ny] is False:
                field[nx][ny] = 'F'
                fire.append((nx, ny))
                f[nx][ny] = True

    for _ in range(len(jh)):
        x, y = jh.popleft()
        visited[x][y] = True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if field[nx][ny] == '.' and visited[nx][ny] is False:
                    field[nx][ny] = 'J'
                    jh.append((nx, ny))
                    visited[nx][ny] = True

            else:
                found = True
                break

        if found:
            break

    if found:
        state = 0
        break

    if len(jh) == 0:
        time = 'IMPOSSIBLE'
        break

print(time)