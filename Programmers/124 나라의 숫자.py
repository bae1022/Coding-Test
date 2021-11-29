def solution(n):
    answer = ''

    share = n

    while share != 0:
        r = share % 3 # 나눈 나머지
        share = share // 3

        if r == 0: # 나누어 떨어질 경우
            answer += '4'
            share -= 1

        elif r == 1: # 나머지가 1일 경우
            answer += '1'

        elif r == 2:
            answer += '2'

    return answer[::-1]

print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 3
print(solution(4)) # 4