import math

def solution(left, right):
    answer = 0

    def count(n):
        cnt = 0

        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1

        return cnt

    for i in range(left, right + 1):
        if count(i) % 2 == 0: # 약수의 개수가 짝수:
            answer += i

        else:
            answer -= i

    return answer

print(solution(13, 17)) # 43
print(solution(24, 27)) # 52