import heapq
INF = 1e9

n, m, r = map(int, input().split()) # 지역 개수, 수색범위, 길의 개수
items = [0] + list(map(int, input().split()))

graph = [[] for i in range(n + 1)]

for i in range(r):
    a, b, l = map(int, input().split())

    graph[a].append((b, l))
    graph[b].append((a, l))

def solve(start): #다익스트라 이용 (한 노드에서 다른 모드 노드까지의 최단 거리를 구함)
        q = []

        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            else:
                for i in graph[now]:
                    cost = dist + i[1]

                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))

answer = -1
for i in range(1, n + 1):
    temp = 0
    distance = [INF] * (n + 1)
    solve(i)
    for j in range(1, n + 1):
        if distance[j] <= m:
            temp += items[j]

    if answer < temp:
        answer = temp

print(answer)