def solution(N, stages):
    answer = []

    fail = [0 for i in range(N + 2)]
    try_n = [0 for i in range(N + 2)]

    result = []
    for stage in stages:
        fail[stage] += 1
        for i in range(1, stage + 1):
            try_n[i] += 1

    for i in range(1, N + 1):
        if fail[i] == 0:
            result.append((i, 0))

        else:
            result.append((i, fail[i] / try_n[i]))

    result.sort(key=lambda x:(-x[1], x[0]))

    for i in range(len(result)):
        answer.append(result[i][0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))