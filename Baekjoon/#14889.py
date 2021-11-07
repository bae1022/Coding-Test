from itertools import combinations

n = int(input())

p = [i for i in range(1, n + 1)]

team = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        team[i + 1][j + 1] = row[j]

choice_team = list(combinations(p, n // 2))

def team_sum(start, link):
    sum_start = 0
    sum_link = 0

    for i in start:
        for j in start:
            sum_start += team[i][j]

    for i in link:
        for j in link:
            sum_link += team[i][j]

    return abs(sum_start - sum_link)

answer = 100000000

for i in range(len(choice_team) // 2):
    start = choice_team[i]
    link = choice_team[len(choice_team) - 1 - i]

    temp = team_sum(start, link)
    answer = min(answer, temp)

print(answer)