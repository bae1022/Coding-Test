from collections import deque

m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny] == 1:
                continue

            elif tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                visit[nx][ny] = 1

                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

bfs()

state = 1
day_max = -1

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            state = -1

        else:
            day_max = max(tomato[i][j], day_max)

if state == -1:
    print(-1)

else:
    print(day_max - 1)
