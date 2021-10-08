from collections import deque

n = int(input()) # 가로, 세로 n

field = []

for _ in range(n):
    field.append(list(map(int, input())))

def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        field[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            else:
                if field[nx][ny] != 0:
                    queue.append((nx, ny))
                    field[nx][ny] = 0
                    cnt += 1

                else:
                    continue

    return cnt

result = []
for i in range(n):
    for j in range(n):
        if field[i][j] != 0:
            answer = bfs(i, j)
            result.append(answer)

result.sort()
print(len(result))
print(*result, sep='\n')