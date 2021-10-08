from collections import deque

t = int(input())

for i in range(t):
    k, m, p = map(int, input().split()) # k: 테스트케이스 번호/ m: 노드 수/p: 간선 수

    graph = [[] for _ in range(m + 1)]

    indegree = [[0, 0, 0] for _ in range(m + 1)] # 진입차수 0으로 초기화

    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)

        indegree[b][0] += 1 # 진입차수 개수 증가

    queue = deque()
    cnt = 1

    for j in range(1, m + 1):
        if indegree[j][0] == 0:
            queue.append(j)

            indegree[j][1] = 1 # 가중치

    while queue:
        now = queue.popleft()

        for l in graph[now]:
            indegree[l][0] -= 1

            if indegree[l][1] < indegree[now][1]: # 가중치 갱신
                indegree[l][1] = indegree[now][1]
                indegree[l][2] = 1 # cnt

            elif indegree[l][1] == indegree[now][1]:
                indegree[l][2] += 1

            if indegree[l][0] == 0: # 처음 들어옴

                if indegree[l][2] > 1:
                    indegree[l][1] += 1
                queue.append(l)


    print(k, indegree[m][1])

