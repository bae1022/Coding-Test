from collections import deque

def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]

    for i in range(len(edge)):
        a, b = edge[i]

        graph[a].append(b)
        graph[b].append(a)

    visit = [-1] * (n + 1)
    visit[1] = 0

    def bfs(x, cnt):
        queue = deque()
        queue.append((x, cnt))

        while queue:
            x, cnt = queue.popleft()

            for i in graph[x]:
                if visit[i] == -1:
                    queue.append((i, cnt + 1))

                    visit[i] = cnt + 1

    bfs(1, 0)

    n_max = max(visit)

    for i in range(len(visit)):
        if visit[i] == n_max:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))