from collections import deque

n, k = map(int, input().split()) # n: 행, 열 크기/k: 바이러스 종류

field = []
virus = []


for i in range(n):
    row = list(map(int, input().split()))
    field.append(row)

    for j in range(n):
        if row[j] != 0:
            virus.append((i, j, row[j], 0))

t, result_x, result_y = map(int, input().split()) # t초 후, (result_x, result_y) 는 무슨 바이러스

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

virus.sort(key=lambda x:x[2])
q = deque(virus)

while q:
    x, y, info, time = q.popleft()
    if time == t:
        break

    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if field[nx][ny] == 0:
                    field[nx][ny] = info
                    q.append((nx, ny, info, time + 1))

print(field[result_x - 1][result_y - 1])