from collections import deque
import sys

n, m = map(int, input().split())

field = [[0] * m for _ in range(n)]
visit = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    row = list(sys.stdin.readline())

    for j in range(m):
        field[i][j] = int(row[j])

queue = deque()
queue.append((0, 0))
visit[0][0] = 1

while queue:
    x, y = queue.popleft()
    visit[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1:
            continue

        elif field[nx][ny] != 0 and visit[nx][ny] == 0:
            queue.append((nx, ny))
            visit[nx][ny] = 1
            field[nx][ny] = field[x][y] + 1

print(field[n - 1][m - 1])