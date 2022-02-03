def solution(sizes):
    answer = 0

    list_long = []
    list_short = []

    for i in range(len(sizes)):
        x, y = sizes[i]

        if x > y:
            list_long.append(x)
            list_short.append(y)

        else:
            list_long.append(y)
            list_short.append(x)

    width = max(list_long)
    height = max(list_short)

    answer = width * height

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))