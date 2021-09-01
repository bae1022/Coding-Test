
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(input()))

min = min(n, m)

result = 0
for i in range(n):
    for j in range(m):
        for k in range(min):
            if i + k < n and j + k < m: # 범위를 벗어나지 않는 경우
                if array[i][j] == array[i][j + k] and array[i][j] == array[i + k][j] and  array[i][j] == array[i + k][j + k]:
                    if result < k:
                        result = k

print((result + 1) * (result + 1))
