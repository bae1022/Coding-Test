n = int(input()) # 사람들의 수
a, b = map(int, input().split()) # 촌수를 계산해야하는 사람들의 번호

m = int(input())

people = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())

    people[x].append(y)
    people[y].append(x)

result = [0] * (n + 1)

def dfs(node):
    for i in people[node]:
        if result[i] == 0:
            result[i] = result[node] + 1
            dfs(i)

dfs(a)

if result[b] == 0:
    print(-1)
else:
    print(result[b])