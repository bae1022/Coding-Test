n, m = map(int, input().split())

train = [[0] * 20 for _ in range(n)]

for _ in range(m):
    l = list(map(int, input().split()))

    if len(l) == 3:
        i = l[1]
        x = l[2]

    elif len(l) == 2:
        i = l[1]

    if l[0] == 1:
        train[i - 1][x - 1] = 1

    elif l[0] == 2:
        train[i - 1][x - 1] = 0

    elif l[0] == 3:
        temp = train[i - 1][:19]
        train[i - 1][1:] = temp

        train[i - 1][0] = 0

    elif l[0] == 4:
        temp = train[i - 1][1:]
        train[i - 1][:19] = temp

        train[i - 1][19] = 0

answer = []
for i in range(len(train)):
    answer.append(str(train[i]))

print(len(set(answer)))