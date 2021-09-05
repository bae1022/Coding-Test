# 예제1_ 전보
# 도시 x, y 서로를 향하는 통로가 설치되어 있어야 전보를 보낼 수 있다. c라는 도시에서 위급 상황이 발생했을 때 전보를 최대한 많이 퍼져나가게 하고자 한다.
# 도시 c에서 보낸 메세지를 받게 되는 도시의 개수와 도시 모두 메세지를 받는 데까지 걸리는 시간은 얼마?

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) # n: 도시의 개수/m: 통로의 개수/c: 메세지를 보내고자 하는 도시

start = c
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트

distance = [INF] * (n + 1) # 최단 거리 테이블 무한으로 초기화

# 모든 간선 정보 입력받음
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a->b : c만큼의 비용

# print(graph)
def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start)) # 시작노드로 가기 위한 비용은 0 (q 배열에(거리, 노드번호) 튜플 삽입))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면

        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼냄

        if distance[now] < dist: # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            continue

        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

max_time = 0
cnt = 0

for i in distance:
    if i == INF:
        continue
    else:
        cnt += 1

        if max_time < i:
            max_time = i

print(cnt - 1, max_time)

