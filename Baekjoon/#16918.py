r, c, n = map(int, input().split())

field = [[('', -1)] * c for _ in range(r)]

for i in range(r):
    col = list(input())

    for j in range(c):
        if col[j] == '.': # 빈 칸
            field[i][j] = (col[j], -1)

        elif col[j] == 'O':
            field[i][j] = (col[j], 3)

def count_down():
    for q in range(r):
        for w in range(c):
            if field[q][w][0] == 'O':
                op, count = field[q][w]

                field[q][w] = ('O', count - 1)

def bomb(x, y): # 폭탄 터짐
    field[x][y] = ('.', -1)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < r and 0 <= ny < c:
            if field[nx][ny][0] == 'O' and field[nx][ny][1] == 0:
                continue
            else:
                field[nx][ny] = ('.', -1)

for i in range(n):
    count_down()  # 카운트다운 실시

    if i == 0: # 처음 1초 동안 아무것도 하지 않는다.
        continue

    elif i % 2 == 1: # 다음 1초 동안 폭탄이 설치되지 않은 모든 칸에 폭탄을 설치한다.
        for a in range(r):
            for b in range(c):
                if field[a][b][0] == '.':
                    field[a][b] = ('O', 3)

    elif i % 2 == 0:
        for a in range(r):
            for b in range(c):
                if field[a][b][0] == 'O' and field[a][b][1] == 0:
                    bomb(a, b)


for i in range(r):
    for j in range(c):
        print(field[i][j][0], end='')

    print()