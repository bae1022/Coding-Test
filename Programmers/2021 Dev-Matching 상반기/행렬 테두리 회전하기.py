def solution(rows, columns, queries):
    answer = []

    field = [[0] * columns for _ in range(rows)]
    cnt = 1

    for i in range(rows):
        for j in range(columns):
            field[i][j] = cnt
            cnt += 1

    for k in range(len(queries)):
        x1 = queries[k][0]
        y1 = queries[k][1]
        x2 = queries[k][2]
        y2 = queries[k][3]

        tmp = field[x1 - 1][y1 - 1]
        mini = tmp

        for k in range(x1 - 1, x2 - 1):
            test = field[k + 1][y1 - 1]
            field[k][y1 - 1] = test
            mini = min(mini, test)

        for k in range(y1 - 1, y2 - 1):
            test = field[x2 - 1][k + 1]
            field[x2 - 1][k] = test
            mini = min(mini, test)

        for k in range(x2 - 1, x1 - 1, -1):
            test = field[k - 1][y2 - 1]
            field[k][y2 - 1] = test
            mini = min(mini, test)

        for k in range(y2 - 1, y1 - 1, -1):
            test = field[x1 - 1][k - 1]
            field[x1 - 1][k] = test
            mini = min(mini, test)

        field[x1 - 1][y1] = tmp
        answer.append(mini)

    return answer

print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))