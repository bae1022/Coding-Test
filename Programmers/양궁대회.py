from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]

    temp = [i for i in range(0, 11)]
    tmp_list = list(combinations_with_replacement(temp, n))

    result = 0

    for i in range(len(tmp_list)):
        lion_score = [0] * 11
        t = list(tmp_list[i])

        for j in range(len(t)):
            tmp = t[j]
            lion_score[10 - tmp] += 1

        lion = 0
        appeach = 0
        # 점수 비교

        for a in range(11):
            if lion_score[a] == 0 and info[a] == 0:
                continue

            if lion_score[a] > info[a]:  # 라이언은 어피치보다 맞춘 횟수가 많아야 점수를 획득할 수 있다.
                lion += 10 - a

            else:
                appeach += 10 - a

        if result < (lion - appeach):
            result = lion - appeach
            answer = lion_score

    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))