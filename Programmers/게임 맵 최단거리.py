from collections import deque

def solution(maps):
    answer = 0

    x_len = len(maps)
    y_len = len(maps[0])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visit = [[-1] * y_len for _ in range(x_len)]

    def bfs(x, y):
        queue = deque()

        cnt = 1
        queue.append((x, y, cnt))
        visit[x][y] = 1

        while queue:
            x, y, cnt = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= x_len or ny < 0 or ny >= y_len:
                    continue

                else:
                    if maps[nx][ny] == 1 and visit[nx][ny] == -1:
                        queue.append((nx, ny, cnt + 1))
                        visit[nx][ny] = cnt + 1

        return cnt

    bfs(0, 0)
    answer = visit[x_len - 1][y_len - 1]

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1