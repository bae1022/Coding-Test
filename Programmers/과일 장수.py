def solution(k, m, score):
    answer = 0

    '''
    사과의 최대 점수: k
    한 상자에 들어가는 사과의 수: M
    사과들의 점수: score
    '''

    score.sort(reverse=True)
    for i in range(m - 1, len(score), m):
        temp = score[i] * m
        answer = answer + temp
    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))