t = int(input())

for _ in range(t):
    n = int(input())
    list_1 = set(list(map(int, input().split())))

    m = int(input())
    list_2 = list(map(int, input().split()))

    for i in range(len(list_2)):
        if list_2[i] in list_1:
            print(1)

        else:
            print(0)

