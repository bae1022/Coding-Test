from itertools import permutations

def solution(k, dungeons): # 현재 피로도, [최소 피로도, 소모 피로도]
    answer = 0

    p = list(permutations(dungeons, len(dungeons)))

    for i in range(len(p)):
        start = k
        temp = 0
        for min_k, minus in p[i]:
            if start < min_k:
                break

            elif start >= min_k:
                start -= minus
                temp += 1

        answer = max(temp, answer)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]])) # 3