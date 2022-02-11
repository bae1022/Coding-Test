student = [0] * 31

for _ in range(28):
    n = int(input())

    student[n] = 1

for i in range(1, 31):
    if student[i] == 0:
        print(i)