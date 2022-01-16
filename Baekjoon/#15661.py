from itertools import combinations

n = int(input())
p = [[0] * n for _ in range(n)]
members = [i for i in range(n)]

for i in range(n):
    t = list(map(int, input().split()))

    for j in range(n):
        p[i][j] = t[j]

possible_team = []
for i in range(1, n):
    for team in list(combinations(members, i)):
        possible_team.append(team)

answer = 10000
for i in range(len(possible_team) // 2):
    team = possible_team[i]

    a = 0
    for j in range(len(team)):
        member = team[j]

        for k in team:
            a += p[member][k]

    team = possible_team[-i - 1] # a팀을 제외한 팀
    b = 0
    for j in range(len(team)):
        member = team[j]

        for k in team:
            b += p[member][k]

    answer = min(answer, abs(a - b))

print(answer)
