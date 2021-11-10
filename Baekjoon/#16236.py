from collections import deque

INF = int(1e9)

n = int(input())

field = [[0] * n for _ in range(n)]
shark = 2  # 현재 상어의 크기
visit = [[-1] * n for _ in range(n)]

now_x = 0
now_y = 0

for i in range(n):
    col = list(map(int, input().split()))

    for j in range(n):
        field[i][j] = col[j]

        if field[i][j] == 9:
            now_x = i
            now_y = j

            field[i][j] = 0  # 상어 정보 저장 후 0으로 바꿈꿈

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    distance = [[-1] * n for _ in range(n)]

    queue = deque()
    queue.append((x, y))

    distance[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            else:
                if distance[nx][ny] == -1 and field[nx][ny] <= shark:
                    # 물고기가 상어보다 작거나 같은 경우는 이동이 가능하다.

                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return distance


def find(distance):
    x, y = 0, 0
    min_dist = INF

    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 1 <= field[i][j] < shark:
                # 도달할 수 있는 거리이며, 먹을 수 있는 물고기라면 (상어의 크기와 같은 물고기는 지나갈 수 있을 뿐, 먹을 수는 없다.)

                if min_dist > distance[i][j]:
                    x, y = i, j
                    min_dist = distance[i][j]

    if min_dist == INF:  # 먹을 수 있는 물고기가 없는 상태이다.
        return None

    else:
        return x, y, min_dist


answer = 0
ate = 0

while True:
    temp = bfs(now_x, now_y)
    value = find(temp)

    if value == None:
        print(answer)
        break

    else:
        now_x, now_y, = value[0], value[1]

        answer += value[2]

        field[now_x][now_y] = 0
        ate += 1

        if ate >= shark:  # 먹을 물고기 크기가 현재 상어 크기보다 크거나 같다면
            shark += 1  # 상어 성장
            ate = 0  # 먹은 수 리셋