n, m = map(int, input().split())

p = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    p[a].append(b)
    p[b].append(a)

def solve(start, depth):
    global state

    if depth == 4:
        state = 1
        return

    for i in p[start]:
        if visited[i] is False:
            visited[i] = True
            solve(i, depth + 1)
            visited[i] = False


visited = [False] * n
for j in range(n):
    visited[j] = True
    state = 0
    solve(j, 0)
    visited[j] = False

    if state == 1:
        print(1)
        break

if state == 0:
    print(0)