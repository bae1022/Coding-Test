from itertools import combinations

n, m = map(int, input().split()) # n은 도시 크기/ m은 치킨집의 개수

city = []

house = []
chicken = []
for i in range(n):
    city = list(map(int, input().split()))

    for j in range(n):
        if city[j] == 1:
            house.append((i, j))

        elif city[j] == 2:
            chicken.append((i, j))

leave_chicken = list(combinations(chicken, m))

answer = 1e9

for chickens in leave_chicken:
    result = 0

    for hx, hy in house:
        temp = 1e9

        for cx, cy in chickens:
            length = abs(hx - cx) + abs(hy - cy)

            if length < temp:
                temp = length

        result += temp

    if answer > result:
        answer = result

print(answer)