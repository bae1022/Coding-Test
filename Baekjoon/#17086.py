from collections import deque

n, m = map(int, input().split())

field = []
for i in range(n):
    field.append(list(map(int, input().split())))

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def solution(n1, n2):
    visit = [[0] * m for _ in range(n)]
    cnt = 0

    queue = deque()
    queue.append((n1, n2, cnt))
    visit[n1][n2] = 1

    while queue:
        x, y, cnt = queue.popleft()

        if field[x][y] == 1:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            else:
                if visit[nx][ny] != 1:
                    queue.append((nx, ny, cnt + 1))
                    visit[nx][ny] = 1

    return cnt

cnt_max = -1
temp = 0
for i in range(n):
    for j in range(m):

        if field[i][j] == 1:
            continue

        else:
            temp = solution(i, j)

            cnt_max = max(temp, cnt_max)

print(cnt_max)