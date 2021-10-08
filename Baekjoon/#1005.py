from collections import deque
import sys

t = int(sys.stdin.readline()) # 테스트케이스의 개수

for _ in range(t):

    n, k = map(int, sys.stdin.readline().split()) # n: 노드 수, k: 간선 수
    graph = [[0] for _ in range(n + 1)]

    indegree = [0 for _ in range(n + 1)]
    weights = [0] + list(map(int, sys.stdin.readline().split()))

    dp = [0 for _ in range(n + 1)] # 해당 건물까지 걸리는 시간

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())

        graph[a].append(b)
        indegree[b] += 1

    w = int(sys.stdin.readline()) # 건설해야할 건물의 번호

    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = weights[i]

    while queue:
        now = queue.popleft()

        for l in graph[now]:
            indegree[l] -= 1
            dp[l] = max(dp[now] + weights[l], dp[l])

            if indegree[l] == 0:
                queue.append(l)

    print(dp[w])