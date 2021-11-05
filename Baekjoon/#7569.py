from collections import deque
import sys

m, n, h = map(int, input().split()) # n: 세로칸 수, m: 가로칸 수, h: 쌓아올려지는 상자의 수

tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[0] * m for _ in range(n)] for _ in range(h)]

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

def bfs():
    while queue:
        z, x, y = queue.popleft()
        visit[z][x][y] = 1

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h or visit[nz][nx][ny] == 1:
                continue

            elif tomato[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                visit[nz][nx][ny] = 1


for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j))

bfs()

state = 0 # 익지 못한 사과가 있는 경우

day_max = -1
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0: # 하나라도 익지 못한 토마토가 있다면
                state = -1

            else:
                day_max = max(day_max, tomato[k][i][j])

    if state == -1:
        break

if state == -1: # 하나라도 익지 못한 사과가 있다.
    print(-1)

else:
    print(day_max - 1)