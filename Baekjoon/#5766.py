from collections import defaultdict

n = -1
m = -1

while n != 0 and m != 0:
    n, m = map(int, input().split())
    p = defaultdict(lambda:0)

    for i in range(n):
        col = list(map(int, input().split()))
        for j in range(m):
            p[col[j]] += 1

    p = dict((sorted(p.items(), key=lambda item:-(item[1]))))

    prev = -1
    tmp = -1
    second = -1
    result = []
    for key, value in p.items():
        if prev == -1:
            prev = value
            continue

        if prev != -1 and value < prev and tmp == -1:
            tmp = value
            result.append(key)
            continue

        if tmp == value:
            result.append(key)

    result = sorted(result)
    print(*result)

