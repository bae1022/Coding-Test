n, m = map(int, input().split()) # n: 파티장의 크기, m: 서비스를 요청한 손님의 수

INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    col = list(map(int, input().split()))

    for j in range(n):
        graph[i + 1][j + 1] = col[j]

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for _ in range(m):
    a, b, c = map(int, input().split())

    if graph[a][b] <= c:
        print('Enjoy other party')

    elif graph[a][b] > c:
        print('Stay here')