
n1, n2 = map(int, input().split()) # n1: 첫번째 그룹의 개미의 수, n2: 두번째 그룹의 개미의 수

ants1 = list(input())
ants2 = list(input())

t = int(input()) # t초 뒤 개미의 상태는?

ants = []

ants1.reverse()

for i in range(len(ants1)):
    ants.append((ants1[i], 0))

for i in range(len(ants2)):
    ants.append((ants2[i], 1))

for _ in range(t):
    i = 0
    while i < len(ants)-1:
        if ants[i][1] == 0 and ants[i + 1][1] == 1:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 1
        i += 1

for i in range(len(ants)):
    print(ants[i][0], end='')