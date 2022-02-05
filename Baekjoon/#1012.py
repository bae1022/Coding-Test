from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n1, n2):
    q = deque()
    q.append((n1, n2))

    while q:
        n1, n2 = q.popleft()
        visited[n1][n2] = True

        for a in range(4):
            nx = n1 + dx[a]
            ny = n2 + dy[a]

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                if visited[nx][ny] is False:
                    q.append((nx, ny))
                    visited[nx][ny] = True

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 수

    field = [[0] * m for _ in range(n)]
    lot = []

    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1
        lot.append((x, y))

    visited = [[False] * m for _ in range(n)]
    answer = 0

    for l in lot:
        x, y = l

        if visited[x][y] is False:
            bfs(x, y)
            answer += 1

    print(answer)