from collections import deque

n, m, k = map(int, input().split()) # n*m 체육관 크기/ k: 1초에 이동할 수 있는 칸의 최대 개수

field = []
for _ in range(n):
    field.append(list(map(str, input())))

x1, y1, x2, y2 = map(int, input().split()) # -1 해줘야함

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

INF = 1e9
visit = [[INF] * m for _ in range(n)]

def solution(n1, n2):

    queue = deque()
    queue.append((n1, n2))

    visit[n1][n2] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nk = 1

            # 방향을 하나 정했으면 끝까지 나아가는 방식 / 2충 for문으로 각 방향에 대해서 나아가는 방식으로는 시간 초과가 난다.
            while nk <= k and nx >= 0 and nx < n and ny >= 0 and ny < m and field[nx][ny] != '#' and visit[nx][ny] > visit[x][y]:
                if visit[nx][ny] == INF:
                    queue.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1

                nx += dx[i]
                ny += dy[i]
                nk += 1

solution(x1 - 1, y1 - 1)

if visit[x2 - 1][y2 - 1] == INF:
    print(-1)

else:
    print(visit[x2 - 1][y2 - 1])