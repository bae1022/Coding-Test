n, m = map(int, input().split()) # 집하장 개수, 경로 개수
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
pre_node = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, l = map(int, input().split())

    graph[a][b] = l
    graph[b][a] = l

    pre_node[a][b] = b
    pre_node[b][a] = a

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
            pre_node[i][j] = '-'

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a = graph[i][j]
            b = graph[i][k] + graph[k][j]

            graph[i][j] = min(a, b)

            if graph[i][j] == a:
                continue

            elif graph[i][j] == b:
                pre_node[i][j] = pre_node[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(pre_node[i][j], end=' ')

    print()