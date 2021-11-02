inputs = [[0] * 15 for _ in range(5)]

n = 5
m = 15

for i in range(n):
    row = list(input())

    for j in range(len(row)):
        inputs[i][j] = row[j]

for j in range(m):
    for i in range(n):
        if inputs[i][j] == 0:
            continue

        else:
            print(inputs[i][j], end='')