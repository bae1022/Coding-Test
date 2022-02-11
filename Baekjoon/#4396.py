n = int(input())

field = [[''] * n for _ in range(n)]
opens = [[''] * n for _ in range(n)]

bomb = []
op = []

for i in range(n):
    col = list(input())

    for j in range(n):
        if col[j] == '*':
            bomb.append((i, j))

        field[i][j] = col[j]

for i in range(n):
    col = list(input())

    for j in range(n):
        if col[j] == 'x':
            op.append((i, j))

        opens[i][j] = col[j]

state = 0
for i in range(len(bomb)):
    x1, x2 = bomb[i]

    for j in range(len(op)):
        y1, y2 = op[j]

        if x1 == y1 and x2 == y2:
            state = -1
            break

    if state == -1:
        break

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(n):
    for j in range(n):

        if state == -1 and field[i][j] == '*':
            opens[i][j] = '*'

        if opens[i][j] == 'x':
            cnt = 0
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]

                if 0 <= ni < n and 0 <= nj < n:
                    if field[ni][nj] == '*':
                        cnt += 1

            opens[i][j] = cnt

for i in range(n):
    for j in range(n):
        print(opens[i][j], end='')

    print()