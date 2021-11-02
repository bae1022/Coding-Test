n = 3
m = 4

for i in range(n):
    row = list(map(int, input().split()))

    cnt = row.count(0) # 배의 개수

    if cnt == 1:
        print('A')

    elif cnt == 2:
        print('B')

    elif cnt == 3:
        print('C')

    elif cnt == 4:
        print('D')

    else:
        print('E')

