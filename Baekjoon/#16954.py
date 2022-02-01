from collections import deque

field = [[''] * 8 for _ in range(8)]

for i in range(8):
    col = input()
    for j in range(8):
        field[i][j] = col[j]

field = deque(field)

def wall_move():
    global field

    field.pop()
    field.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

x = 7
y = 0

dx = [0, -1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 0, -1, 1, -1, 1, -1, 1]

q = deque()
q.append((x, y))

visited = [[False] * 8 for _ in range(8)]
state = -1

while q:
    visited = [[False] * 8 for _ in range(8)]

    for _ in range(len(q)):
        x, y = q.popleft()

        if field[x][y] == '#': # 벽 충돌 (진행 불가)
            continue

        if x == 0 and y == 7:
            state = 0
            break

        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 8 and 0 <= ny < 8:
                if visited[nx][ny] is False and field[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))

    wall_move()

    if state == 0:
        break

if state == -1:
    print(0)
else:
    print(1)
