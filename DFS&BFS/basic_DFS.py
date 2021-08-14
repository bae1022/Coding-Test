# DFS 기본

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end='')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 배열 0번째 자리는 공백으로 표시
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9 # 배열 0번째가 공백이므로, +1을 한 9를 곱해줌
dfs(graph, 1, visited)