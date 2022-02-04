from collections import deque

n, m = map(int, input().split())

field = [[0] * m for _ in range(n)]

total_ice = 0

for i in range(n):
    col = list(map(int, input().split()))
    for j in range(m):
        field[i][j] = col[j]

        if col[j] != 0:
            total_ice += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    global total_ice
    global ice_x
    global ice_y

    melt_cnt = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if field[x][y] != 0: # 얼음 발견

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0:
                        melt_cnt[x][y] += 1

    for i in range(n):
        for j in range(m):
            if field[i][j] != 0:
                field[i][j] -= melt_cnt[i][j]

                if field[i][j] <= 0:
                    field[i][j] = 0
                    total_ice -= 1

                else:
                    ice_x = i
                    ice_y = j

def check_ice(x, y):
    cnt = 1

    q = deque()
    q.append((x, y))

    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] != 0:
                if visited[nx][ny] is False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1

    return cnt

answer = 0
state = -1

ice_x = 0
ice_y = 0

while True:
    melt()

    if total_ice == 0:
        break

    c = check_ice(ice_x, ice_y)

    if total_ice - c == 0: # 아직 얼음이 한 덩어리
        answer += 1
        continue

    else: # 얼음이 동강 났음
        state = 0
        break

if state == 0:
    print(answer + 1)

else:
    print(0)
