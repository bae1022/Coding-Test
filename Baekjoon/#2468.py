from collections import deque

n = int(input())

field = [[0] * n for _ in range(n)]

min_wall = 101
max_wall = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        field[i][j] = row[j]

        min_wall = min(min_wall, row[j])
        max_wall = max(max_wall, row[j])

# print(field)
# print(min_wall)
# print(max_wall)

def bfs(x, y, water):
    queue = deque()

    queue.append((x, y))
    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            elif field[nx][ny] > water and visit[nx][ny] == 0:
                queue.append((nx, ny))
                visit[nx][ny] = 1

answer = 0

if min_wall == max_wall:
    print(1)
else:
    for k in range(min_wall, max_wall):
        visit = [[0] * n for _ in range(n)]
        temp = 0

        for i in range(n):
            for j in range(n):
                if visit[i][j] == 0 and field[i][j] > k:
                    bfs(i, j, k)
                    temp += 1

        answer = max(temp, answer)

    print(answer)