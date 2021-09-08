n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

distance = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)

    for a, b, c in arr: # a: 시작/b: 도착/c: 비용
        if i == a and b <= d and distance[i] + c < distance[b]:
            distance[b] = distance[i] + c

print(distance[d])