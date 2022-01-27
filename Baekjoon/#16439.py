from itertools import combinations

n, m = map(int, input().split()) # 회원 수, 치킨 수

c = [i for i in range(m)]
chicken = [[0] * m for _ in range(n)]

prefer_list = list(combinations(c, 3))

for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(m):
        chicken[i][j] = temp[j]

answer = -1

for p in prefer_list:
    a, b, c = p
    temp = 0

    for i in range(n):
        c1, c2, c3 = chicken[i][a], chicken[i][b], chicken[i][c]

        t_max = max(c1, c2, c3)
        temp += t_max

    if answer < temp:
        answer = temp

print(answer)
