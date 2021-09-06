# 예제2_ 미래도시
# 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표이며, 빠르게 이동하고자 할 때 최소 시간을 구하라
INF = int(1e9)

n, m = map(int, input().split()) # n: 전체 회사의 개수/ m: 경로의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트 만들고 무한 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대하 정보를 입력받아 초기화
for _ in range(m):
    a, b = map(int, input().split()) # a에서 b로 가는 비용은 c
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split()) # x: 최종 목적지/k: 경유할 회사

# for i in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
