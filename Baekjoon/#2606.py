n = int(input()) # 컴퓨터 수
m = int(input()) # 컴퓨터 연결 쌍의 수

visited = [-1] * (n + 1)
com = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    com[a].append(b)
    com[b].append(a)

answer = 0
def dfs(num):
    global answer

    l = com[num]

    if len(l) == 0:
        return answer

    while l:
        tmp = l[-1]

        if visited[tmp] == -1:
            visited[tmp] = 1

            l.pop()
            answer += 1

            dfs(tmp)

        else:
            l.pop()

dfs(1)
print(answer - 1)