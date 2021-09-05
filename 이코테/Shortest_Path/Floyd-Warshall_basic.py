INF = int(1e9) # 무한을 의미

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트 만들고 무한 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대하 정보를 입력받아 초기화
for _ in range(m):
    a, b, c = map(int, input().split()) # a에서 b로 가는 비용은 c
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                                            # a에서 k를 거쳐 b로 가는 비용

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")

        else:
            print(graph[a][b], end=" ")

    print()