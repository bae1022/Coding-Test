from collections import deque

k = int(input())
w, h = map(int, input().split())

field = [[0] * w for _ in range(h)]

for i in range(h):
    col = list(map(int, input().split()))

    for j in range(w):
        field[i][j] = col[j]

horse_x = [-2, -1, 1, 2, 2, 1, -1, -2] # 말의 움직임
horse_y = [-1, -2, -2, -1, 1, 2, 2, 1] # 말의 움직임

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

state = 0
answer = -1

visit = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]

def solve(x, y):
    global state
    global answer

    q = deque()
    q.append((x, y, 0, k))

    while q:
        x, y, cnt, kk = q.popleft()

        if x == h - 1 and y == w - 1:
            state = 1
            answer = cnt
            break

        if kk > 0:
            for hor in range(8):
                nx = x + horse_x[hor]
                ny = y + horse_y[hor]

                if 0 <= nx < h and 0 <= ny < w:
                    if field[nx][ny] == 0 and visit[nx][ny][kk - 1] == 0:
                        q.append((nx, ny, cnt + 1, kk - 1))
                        visit[nx][ny][kk - 1] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if field[nx][ny] == 0 and visit[nx][ny][kk] == 0:
                    q.append((nx, ny, cnt + 1, kk))
                    visit[nx][ny][kk] = 1

solve(0, 0)

if state == 1:
    print(answer)

else:
    print(-1)
