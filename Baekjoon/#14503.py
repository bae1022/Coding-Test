n, m = map(int, input().split())

field = [[0] * m for _ in range(n)]

r, c, d = map(int, input().split()) # (r, c) , 0: 북/ 1: 동/2: 남/3: 서

for i in range(n):
    col = list(map(int, input().split()))

    for j in range(m):
        field[i][j] = col[j]

answer = 0

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]

def clean(d, x, y):
    global answer

    if field[x][y] == 0: # 빈 공간이면
        field[x][y] = 2
        answer += 1

    for _ in range(4):
        nd = (d + 3) % 4 # 방향 변경

        nx = x + dx[nd]
        ny = y + dy[nd]

        if field[nx][ny] == 0: # 청소할 공간이 있다면
            clean(nd, nx, ny) # 첫 부분으로
            return

        d = nd # 청소할 부분이 없는 경우 방향을 유지한 채로 뒤로 후진해야 한다.

    nd = (d + 2) % 4 # 후진을 위한 방향 설정

    nx = x + dx[nd]
    ny = y + dy[nd]

    if field[nx][ny] == 1: # 후진할 방향에 벽이 있다면
        return

    clean(d, nx, ny) # 후진한 채로 재탐색

clean(d, r, c)
print(answer)