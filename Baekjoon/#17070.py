import sys

n = int(input())

home = [[0] * n for _ in range(n)]
answer = 0

def dfs(x, y, dir):
    global answer

    if x == n - 1 and y == n - 1:
        answer += 1
        return

    if dir == 0: # 가로방향
        if y + 1 < n and home[x][y + 1] == 0:
            dfs(x, y + 1, 0) # 가로

        if x + 1 < n and y + 1 < n and home[x + 1][y] == 0 and home[x][y + 1] == 0 and home[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2) # 대각

    if dir == 1: # 세로방향
        if x + 1 < n and home[x + 1][y] == 0:
            dfs(x + 1, y, 1)

        if x + 1 < n and y + 1 < n and home[x + 1][y] == 0 and home[x][y + 1] == 0 and home[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)  # 대각

    if dir == 2: # 대각방향
        if y + 1 < n and home[x][y + 1] == 0:
            dfs(x, y + 1, 0) # 가로

        if x + 1 < n and home[x + 1][y] == 0:
            dfs(x + 1, y, 1)

        if x + 1 < n and y + 1 < n and home[x + 1][y] == 0 and home[x][y + 1] == 0 and home[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)  # 대각

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        home[i][j] = a[j]

dfs(0, 1, 0)
print(answer)