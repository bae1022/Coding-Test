def solution(N, road, K):
    answer = 0

    n = N # 노드의 수
    m = len(road) # 간선의 수
    INF = 1e9

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for i in range(m):
        a, b, c = road[i]

        if graph[a][b] == INF:
            graph[a][b] = c
            graph[b][a] = c

        if graph[a][b] != INF and c < graph[a][b]:
            graph[a][b] = c
            graph[b][a] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        if graph[1][i] <= K:
            answer += 1

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 3
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4