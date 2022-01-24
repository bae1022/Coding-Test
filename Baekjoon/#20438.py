n, k, q, m = map(int, input().split())

student = [0] * (n + 3)

sleep = list(map(int, input().split()))

for i in sleep:
    student[i] = -1 # 자는 학생 체크

code = list(map(int, input().split()))

area = []
for i in range(m):
    start, end = map(int, input().split())
    area.append((start, end))

for i in code:
    k = 1

    if student[i] != -1: # 자고 있는 경우가 아니라면
        while i * k < n + 3:
            if student[i * k] != -1:
                student[i * k] = 1

            k += 1

sum_arr = [0] * (n + 3)

for i in range(3, n + 3):
    tmp = student[i]

    if tmp == -1:
        tmp = 0

    sum_arr[i] = sum_arr[i - 1] + tmp

for i in area:
    start, end = i

    print((end - start + 1) - (sum_arr[end] - sum_arr[start - 1]))