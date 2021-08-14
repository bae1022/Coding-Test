# 예제 1
# 음료수 얼려 먹기_ N*M 크기의 얼음틀이 있고, 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수?

# dfs로 특정 노드 방문하고 연결된 모든 노드들도 방문한다.
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 주어진 범위 벗어나면 종료
        return False

    if graph[x][y] == 0: # 현재 노드를 방문하지 않았다면

        graph[x][y] = 1 # 노드 방문 처리

    # 상, 하, 좌, 우 위치들 모두 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

