from itertools import combinations

n = int(input())
cost = [[0] * n for _ in range(n)]


tmp = []
for i in range(n):
    col = list(map(int, input().split()))
    for j in range(n):
        cost[i][j] = col[j]
        tmp.append((i, j))
l = list(combinations(tmp, 3))

answer = 2000000000
for i in range(len(l)):
    field = [[0] * n for _ in range(n)]
    tmp = 0
    state = 0

    for j in range(len(l[i])):
        x, y = l[i][j]

        if 0 <= x - 1 < n and 0 <= y - 1 < n and 0 <= x + 1 < n and 0 <= y + 1 < n and field[x][y] != 1:
            if field[x - 1][y] == 1 or field[x + 1][y] == 1 or field[x][y - 1] == 1 or field[x][y + 1] == 1:
                state = -1
                break

            else:
                tmp += cost[x][y]
                tmp += cost[x - 1][y]
                tmp += cost[x + 1][y]
                tmp += cost[x][y - 1]
                tmp += cost[x][y + 1]

                field[x][y] = 1
                field[x - 1][y] = 1
                field[x + 1][y] = 1
                field[x][y - 1] = 1
                field[x][y + 1] = 1

        else:
            state = -1
            break

    if state == -1:
        continue

    else:
        answer = min(answer, tmp)

print(answer)