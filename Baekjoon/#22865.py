import heapq
from sys import stdin

INF = int(10e9)

n = int(stdin.readline())
x, y, z = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]

m = int(stdin.readline())

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

def solve(graph, start):
    distance = [INF] * len(graph)
    distance[start] = 0
    heap = [[0, start]]

    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                heapq.heappush(heap, [distance[next_node], next_node])

    return distance

dist_x = solve(graph, x)
dist_y = solve(graph, y)
dist_z = solve(graph, z)

max_value = -1
for i in range(1, n + 1):
    if max_value < min(dist_x[i], dist_y[i], dist_z[i]):
        max_value = min(dist_x[i], dist_y[i], dist_z[i])
        answer = i

print(answer)
