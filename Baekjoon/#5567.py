from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
result = [0] * (n + 1)

visited[1] = 1
queue = deque()

def dfs(node):

    for i in graph[node]:
        if visited[i] == 0:
            result[i] = result[node] + 1
            visited[i] = 1
            queue.append(i)

    while queue:
        dfs(queue.popleft())

dfs(1)

answer = 0
for i in range(len(result)):
    if 0 < result[i] <= 2:
        answer += 1

print(answer)