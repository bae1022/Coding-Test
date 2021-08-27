# 예제 2
# 미로 탈출_ 현재 위치는 (1, 1)이며 미로의 출구는 (N, M), 한 번에 한 칸씩 이동할 수 있다. 괴물이 있는 부분은 0으로 표시한다. 탈출하기 위해 움직여야 하는 최소 칸의 개수?

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 공간을 벗어난 경우 무시
                continue

            if graph[nx][ny] == 0: # 괴물 마주치면 무시
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))

