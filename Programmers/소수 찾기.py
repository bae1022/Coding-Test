import math

def solution(n):
    answer = 0

    temp = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n) + 1)):
        if temp[i]:  # 소수라면
            for j in range(i + i, n + 1, i):  # 소수의 배수는 소수가 아니다.
                temp[j] = False

    for i in range(2, n + 1):
        if temp[i]:
            answer += 1

    return answer

print(solution(10))
print(solution(5))
