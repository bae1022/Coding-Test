from itertools import combinations
from collections import deque

n, m = map(int, input().split())

field = [[0] * m for _ in range(n)]

zero = []
for i in range(n):
    row = list(map(int, input().split()))

    for j in range(m):
        field[i][j] = row[j]

        if row[j] == 0:
            zero.append((i, j))

choice_zero = list(combinations(zero, 2))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 1
    state = 0

    queue = deque()
    queue.append((x, y))

    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny] == 1:
                continue

            else:
                if field[nx][ny] == 0: # 빈칸일 경우 state를 바꾸고 break
                    state = -1

                if field[nx][ny] == 2:
                    cnt += 1
                    queue.append((nx, ny))
                    visit[nx][ny] = 1

    if state == -1:
        cnt = 0

    return cnt

answer = -1
for i in range(len(choice_zero)):
    choice = choice_zero[i]

    choice_1 = choice_zero[i][0]
    choice_2 = choice_zero[i][1]

    choice_1_x = choice_zero[i][0][0]
    choice_1_y = choice_zero[i][0][1]
    choice_2_x = choice_zero[i][1][0]
    choice_2_y = choice_zero[i][1][1]

    field[choice_1_x][choice_1_y] = 1
    field[choice_2_x][choice_2_y] = 1

    visit = [[0] * m for _ in range(n)]

    t = 0

    for j in range(n):
        for k in range(m):

            if field[j][k] == 2 and visit[j][k] == 0:
                temp = bfs(j, k)

                t += temp

    answer = max(answer, t)
    field[choice_1_x][choice_1_y] = 0
    field[choice_2_x][choice_2_y] = 0

if answer == -1:
    print(0)

else:
    print(answer)