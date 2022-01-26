from collections import deque

n, k = map(int, input().split())
water = list(map(int, input().split())) # 샘의 위치들

q = deque()
visited = dict()

for i in water:
    q.append(i)
    visited[i] = 0

while q:
    if k <= 0:
        break

    x = q.popleft()
    dx = [-1, 1]

    for i in range(2):
        nx = x + dx[i]

        if nx not in visited and k > 0:
            visited[nx] = visited[x] + 1
            k -= 1

            q.append(nx)

answer = 0
for key, value in visited.items():
    answer += value

print(answer)
