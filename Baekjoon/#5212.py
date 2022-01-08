r, c = map(int, input().split())

map = [['.'] * c for _ in range(r)]
visit = [[-1] * c for _ in range(r)]

for i in range(r):
    col = list(input())

    for j in range(c):
        map[i][j] = col[j]

for i in range(r):
    for j in range(c):
        cnt = 0
        if map[i][j] == 'X':
            if (0 <= i - 1 < r) and (0 <= j < c):
                if map[i - 1][j] == '.' and visit[i - 1][j] == -1:
                    cnt += 1

            else:
                cnt += 1

            if (0 <= i + 1 < r) and (0 <= j < c):
                if map[i + 1][j] == '.' and visit[i + 1][j] == -1:
                    cnt += 1

            else:
                cnt += 1

            if (0 <= i < r) and (0 <= j - 1 < c):
                if map[i][j - 1] == '.' and visit[i][j - 1] == -1:
                    cnt += 1

            else:
                cnt += 1

            if (0 <= i < r) and (0 <= j + 1 < c):
                if map[i][j + 1] == '.' and visit[i][j + 1] == -1:
                    cnt += 1

            else:
                cnt += 1

        if cnt >= 3:
            map[i][j] = '.'
            visit[i][j] = 0

x = []
y = []

for i in range(r):
    for j in range(c):
        if map[i][j] == 'X':
            x.append(i)
            y.append(j)

max_x = max(x)
min_x = min(x)
max_y = max(y)
min_y = min(y)

for i in range(min_x, max_x + 1):
    tmp = ''
    for j in range(min_y, max_y + 1):
        state = -1
        for k in range(len(x)):
            if i == x[k] and j == y[k]:
                state = 0
                tmp += 'X'
                break

            else:
                continue

        if state == -1:
            tmp += '.'
    print(tmp)