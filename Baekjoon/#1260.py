from collections import deque

n, m, start = map(int, input().split()) # n:정점의 개수/m: 간선의 개수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x1, x2 = map(int, input().split())
    graph[x1].append(x2)
    graph[x2].append(x1)

    graph[x1].sort()
    graph[x2].sort()

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)

visited = [False] * (n + 1)
dfs(start, visited)

print()

visited = [False] * (n + 1)
bfs(start, visited)

