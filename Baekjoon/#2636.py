from collections import deque

n, m = map(int, input().split())
cheese = [[0] * m for _ in range(n)]

for i in range(n):
    cheese[i][:] = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 1

result = []
answer = 0
def melt():
    visited = [[False] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0)) # 0, 0 부터 시작해서 가장자리 공기만 탐색한다. 만약, 0인 것으로 찾게 되면 공기에 노출되지 않은 치즈까지 녹는다.

    visited[0][0] = True
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheese[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                elif cheese[nx][ny] == 1:
                    cheese[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = True

    result.append(cnt)
    return cnt

while True:
    answer += 1
    cnt = melt()

    if cnt == 0:
        break

print(answer - 1)
print(result[-2])
