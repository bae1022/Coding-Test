n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

answer = 0

def dfs(num):
    for j in graph[num]:
        if visited[j] is False:
            visited[j] = True
            dfs(j)
    return

for i in range(1, n + 1):
    if visited[i] is False:
        visited[i] = True
        dfs(i)
        answer += 1

    else:
        continue

print(answer)
