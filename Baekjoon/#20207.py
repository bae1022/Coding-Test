n = int(input())

cal = [[0] * 366 for _ in range(n)]
day = []
for _ in range(n):
    s, e = map(int, input().split())

    day.append((s, e))

day.sort(key=lambda x:(x[0], -(x[1] - x[0] + 1)))

for i in range(len(day)):
    s, e = day[i]

    cnt = 0
    while True:
        state = 0

        for k in range(s, e + 1):
            if cal[cnt][k] == 1:
                state = -1
                break

            else:
                continue

        if state == -1:
            cnt += 1
            continue

        else:
            cal[cnt][s:e + 1] = [1] * (e - s + 1)
            break

row = 0
col = 0
answer = 0
for j in range(1, 366):
    check = False

    for i in range(n):
        if cal[i][j] == 1:
            check = True
            row = max(row, i + 1)

    if check:
        col += 1

    else:
        answer += (row * col)

        row = 0
        col = 0

if check:
    answer += row * col

print(answer)
