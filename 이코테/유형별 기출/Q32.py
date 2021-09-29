n = int(input())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = []

cnt = 2
for i in range(1, n):
    for j in range(cnt):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j]

        elif j == cnt - 1:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]

        else:
            triangle[i][j] = triangle[i][j] + max(triangle[i - 1][j - 1], triangle[i - 1][j])

    cnt += 1

print(max(triangle[len(triangle) - 1]))
