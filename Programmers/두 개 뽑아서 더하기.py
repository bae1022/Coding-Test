from itertools import combinations

def solution(numbers):
    answer = []

    p = list(combinations(numbers, 2))

    for a, b in p:
        temp = a + b
        answer.append(temp)

    answer = list(set(answer))
    answer.sort()

    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))