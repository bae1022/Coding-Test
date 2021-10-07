from collections import deque

n, m = map(int, input().split()) # n: 세로, m: 가로

field = []
coin = []

visit1 = [[0] * m for _ in range(n)]
visit2 = [[0] * m for _ in range(n)]

for i in range(n):

    field.append(list(map(str, input())))

    for j in range(m):
        if field[i][j] == 'o':
            coin.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x1, y1, x2, y2):
    queue = deque()

    cnt = 0

    queue.append((x1, y1, x2, y2, cnt))

    visit1[x1][y1] += 1
    visit2[x2][y2] += 1

    while queue:

        x1, y1, x2, y2, cnt = queue.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]

            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if nx1 >= 0 and nx1 < n and ny1 >= 0 and ny1 < m and nx2 >= 0 and nx2 < n and ny2 >= 0 and ny2 < m:
                if field[nx1][ny1] == '#':
                    nx1 = x1
                    ny1 = y1

                if field[nx2][ny2] == '#':
                    nx2 = x2
                    ny2 = y2

                queue.append((nx1, ny1, nx2, ny2, cnt + 1))

            elif nx1 >= 0 and nx1 < n and ny1 >= 0 and ny1 < m: # 동전1만 보드 위에 올라감
                return cnt + 1

            elif nx2 >= 0 and nx2 < n and ny2 >= 0 and ny2 < m: # 동전1만 보드 위에 올라감
                return cnt + 1

            else: # 둘 다 보드 위에 없는 경우에는 무시
                continue

    return -1

print(bfs(coin[0][0], coin[0][1], coin[1][0], coin[1][1]))