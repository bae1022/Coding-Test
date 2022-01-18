from collections import deque

n, m = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    graph[b].append(a)

def bfs(num):
    visited = [-1] * (n + 1)
    visited[num] = 0

    queue = deque()
    queue.append(num)

    cnt = 1

    while queue:
        x = queue.popleft()

        for j in graph[x]:
            if visited[j] == -1:
                visited[j] = 0
                cnt += 1

                queue.append(j)

    return cnt

tmp = -1
for i in range(1, n + 1):
    c = bfs(i)

    if tmp < c:
        answer = [i]
        tmp = c

    elif tmp == c:
        answer.append(i)

print(*answer)