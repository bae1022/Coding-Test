from collections import deque

n, m, k = map(int, input().split()) # n: 세로 길이 / m: 가로 길이/ k: 음식물 쓰레기의 개수

trash = []
field = [['.'] * (m) for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    trash.append((x, y))

    field[x - 1][y - 1] = '#'

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(x, y):
    result = 0

    queue = deque()
    queue.append((x, y))

    field[x][y] = '.'
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if field[nx][ny] == '#':
                queue.append((nx, ny))
                field[nx][ny] = '.'
                result += 1

    return result + 1

answer = 0

for i in range(n):
    for j in range(m):
        if field[i][j] != '.':
            answer = max(answer, solution(i, j))

print(answer)