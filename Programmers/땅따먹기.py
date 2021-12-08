def solution(land):
    answer = 0

    for i in range(1, len(land)):
        l = land[i - 1]
        for j in range(len(land[0])):
            temp_list = l[:]

            del temp_list[j]

            temp_max = max(temp_list)
            land[i][j] = land[i][j] + temp_max

    answer = max(land[len(land) - 1])

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])) # 16