import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def dfs(num):
    for j in graph[num]:
        if answer[j] == 0:
            answer[j] = num

            dfs(j)

dfs(1)
for i in range(2, n + 1):
    print(answer[i])
