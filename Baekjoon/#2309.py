from itertools import combinations

p = []

for i in range(9):
    p.append(int(input()))

choices = list(combinations(p, 7))

for choice in choices:
    tmp = sum(choice)

    if tmp == 100:
        result = choice

result = list(result)
result.sort()

for r in result:
    print(r)