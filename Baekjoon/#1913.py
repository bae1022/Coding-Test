n = int(input())
m = int(input())

result = [[0] * n for _ in range(n)]

cnt = n * n
d = 0 # 0: 아래, 1: 오른, 2: 위, 3: 왼

i = 0
j = 0
while True:
    if cnt == 0:
        break

    if d == 0:
        for a in range(n):
            if result[a][j] == 0:
                result[a][j] = cnt
                cnt -= 1

                temp_i = a

        d = 1
        i = temp_i

        continue

    elif d == 1:
        for a in range(n):
            if result[i][a] == 0:
                result[i][a] = cnt
                cnt -= 1

                temp_j = a

        d = 2
        j = temp_j
        continue

    elif d == 2:
        for a in range(n - 1, -1, -1):
            if result[a][j] == 0:
                result[a][j] = cnt
                cnt -= 1

                temp_i = a

        d = 3
        i = temp_i

    elif d == 3:
        for a in range(n - 1, -1, -1):
            if result[i][a] == 0:
                result[i][a] = cnt
                cnt -= 1

                temp_j = a

        d = 0
        j = temp_j

answer_i = 0
answer_j = 0
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')

        if result[i][j] == m:
            answer_i = i + 1
            answer_j = j + 1

    print()

print(answer_i, answer_j)