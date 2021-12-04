from collections import deque

def solution(places):
    answer = []

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    def bfs(place):
        start = []

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    start.append((i, j))

        for start_x, start_y in start:
            queue = deque()
            visited = [[False] * 5 for _ in range(5)]

            queue.append((start_x, start_y, 0))
            visited[start_x][start_y] = True

            while queue:
                x, y, d = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    nd = d + 1

                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue

                    else:
                        if visited[nx][ny]:
                            continue

                        else:
                            if place[nx][ny] == 'O':
                                queue.append((nx, ny, nd))
                                visited[nx][ny] = True

                            if place[nx][ny] == 'P' and d <= 1:
                                return 0

        return 1


    for p in places:
        answer.append(bfs(p))
        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# [1, 0, 1, 1, 1]