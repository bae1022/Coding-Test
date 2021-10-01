from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split()) # n: 가로 크기/ m: 세로 크기

field = []
# field = [list(sys.stdin.readline().strip()) for _ in range(m)]
for i in range(m):
    field.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result_W = 0
result_B = 0


def solution(x, y, color):
    cnt = 0

    queue = deque()
    queue.append((x, y))

    field[x][y] == 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if field[nx][ny] != 0 and field[nx][ny] == color:
                queue.append((nx, ny))
                field[nx][ny] = 0
                cnt += 1

    return (1 if cnt==0 else cnt)

for i in range(m):
    for j in range(n):
        if field[i][j] != 0:
            if field[i][j] == 'W':
                result_W += solution(i, j, 'W') ** 2

            elif field[i][j] == 'B':
                result_B += solution(i, j, 'B') ** 2

print(result_W, result_B)
