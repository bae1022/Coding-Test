n, k = map(int, input().split())
distance = list(map(int, input().split()))

temp = 0
i = 0
cnt = 0

while True:
    if temp > k:
        break

    if cnt >= n:
        i = (n * 2 - 1) - cnt

    else:
        i = cnt

    temp += distance[i]
    cnt += 1

print(i + 1)