t = int(input())

def dfs(start, now):
    if visited[now]: # 현재 노드가 방문된 이력이 있고
        if start == now: # 시작지점과 같다면
            return True # 사이클이 존재하는 것

        return False # 시작지점과 다르다면 사이클이 아니다.

    visited[now] = True # 방문 표시

    for node in graph[now]:
        if dfs(start, node):
            return True

    return False

for i in range(t):
    n = int(input())

    n_start = [i for i in range(1, n + 1)]
    n_end = list(map(int, input().split()))

    edges = []

    for j in range(len(n_start)):
        edges.append((n_start[j], n_end[j]))

    graph = [[] for _ in range(n + 1)]

    for edge in edges:
        v, w = edge
        graph[v].append(w)

    answer = 0
    visited = [False] * (n + 1)  # 방문기록

    for k in range(1, n + 1):
        if visited[k]:
            continue

        if dfs(k, k):
            answer += 1

    print(answer)