from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []

    info_dict = defaultdict(list)

    for i in range(len(info)):
        ii = info[i].split()

        dict_key = ii[:-1]
        dict_val = ii[-1]

        for j in range(5): # key로 만들 수 있는 조합을 모두 생성
            combi = list(combinations(dict_key, j))

            for k in range(len(combi)):
                temp = ''.join(combi[k])

                info_dict[temp].append(int(dict_val))

    for k in info_dict:
        info_dict[k].sort()

    for i in range(len(query)):
        q = query[i].split(' ')

        q_key = q[:-1]
        q_val = q[-1]

        while 'and' in q_key:
            q_key.remove('and')

        while '-' in q_key:
            q_key.remove('-')

        q_key = ''.join(q_key)

        if q_key in info_dict:
            score = info_dict[q_key]

            if score:
                s = bisect_left(score, int(q_val)) # 이분탐색으로 찾음
                answer.append(len(score) - s)

        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# [1, 1, 1, 1, 2, 4]