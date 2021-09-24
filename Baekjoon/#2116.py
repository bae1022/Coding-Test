import copy

n = int(input()) # 주사위 개수

dices = []
dices_copy = []


for i in range(n):
    a = list(map(int, input().split()))

    dices.append(a)

if n == 0:
    print(0)

else:
    answer = 0

    for i in range(1, 7): # 첫 번째 주사위를 1~6까지
        start = dices[0].index(i) # 아랫면

        dices_copy = copy.deepcopy(dices)

        result = []
        if start == 0:
            temp = dices_copy[0][5] # 윗면
            del dices_copy[0][5]

        elif start == 1:
            temp = dices_copy[0][3]
            del dices_copy[0][3]

        elif start == 2:
            temp = dices_copy[0][4]
            del dices_copy[0][4]

        elif start == 3:
            temp = dices_copy[0][1]
            del dices_copy[0][1]

        elif start == 4:
            temp = dices_copy[0][2]
            del dices_copy[0][2]

        elif start == 5:
            temp = dices_copy[0][0]
            del dices_copy[0][0]

        dices_copy[0].remove(i)

        result.append(max(dices_copy[0]))

        for j in range(1, n):
            index = dices[j].index(temp)

            if index == 0:
                t = dices_copy[j][5]
                del dices_copy[j][5]

            elif index == 1:
                t = dices_copy[j][3]
                del dices_copy[j][3]

            elif index == 2:
                t = dices_copy[j][4]
                del dices_copy[j][4]

            elif index == 3:
                t = dices_copy[j][1]
                del dices_copy[j][1]

            elif index == 4:
                t = dices_copy[j][2]
                del dices_copy[j][2]

            elif index == 5:
                t = dices_copy[j][0]
                del dices_copy[j][0]

            dices_copy[j].remove(temp)
            temp = t

            result.append(max(dices_copy[j]))

        result = sum(result)

        answer = max(result, answer)


    print(answer)