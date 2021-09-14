from collections import deque

n, m, k, x = map(int, input().split()) # 도시의 개수/도로의 개수/거리정보/출발 도시의 번호

road = []

graph = [[] for i in range(n + 1)] # 0번은 비워두기 위함으로 n + 1 설정

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1) # 모든 도시에 대한 거리 초기화
distance[x] = 0 # 출발 도시까지의 거리는 0

q = deque([x])

while q:
    now = q.popleft()

    for next_n in graph[now]:
        if distance[next_n] == -1:
            distance[next_n] = distance[now] + 1
            q.append(next_n)

result = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        result = True

if result is False:
    print(-1)