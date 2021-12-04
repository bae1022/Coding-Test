import heapq

def solution(land, height):
    answer = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    n = len(land)
    visit = [[-1] * n for _ in range(n)]
    heap = [[0, 0, 0]] # 비용, x, y

    while heap:
        v, x, y = heapq.heappop(heap)

        if visit[x][y] != -1:
            continue

        visit[x][y] = 1
        answer += v

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            else:
                if visit[nx][ny] == -1:
                    if abs(land[x][y] - land[nx][ny]) > height:
                        heapq.heappush(heap, [abs(land[x][y] - land[nx][ny]), nx, ny])

                    else:
                        heapq.heappush(heap, [0, nx, ny])

    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))