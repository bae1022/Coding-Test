INF = int(1e9)

n, m = map(int, input().split()) # n: 유저 수/m: 친구 관계의 수

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

total_part = 0
total = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            continue
        else:
            total_part += graph[i][j]

    total.append(total_part)
    total_part = 0

result = min(total)
print(total.index(result) + 1)