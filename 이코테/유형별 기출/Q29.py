
n, c = map(int, input().split())

n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort()

start = 1
end = n_list[-1] - n_list[0]
result = 0

while (start <= end):
    mid = (start + end) // 2 # gap 의미
    value = n_list[0]
    count = 1

    for i in range(1, n):
        if n_list[i] >= value + mid:
            value = n_list[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

print(result)