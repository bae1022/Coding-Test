import string

def solution(n, t, m, p): # 진법, 말해야 하는 숫자의 개수, 게임 참가 인원, 튜브으 ㅣ순서

    answer = ''

    c = string.digits+string.ascii_uppercase
    def change(num, base): # 진수변환
        q, r = divmod(num, base)

        if q == 0:
            return c[r]
        else:
            return change(q, base) + c[r]

    temp = '0'

    limit = t * m
    i = 1
    while len(temp) <= limit:
        tmp = change(i, n)

        temp += tmp
        i += 1

    p -= 1
    answer += temp[p]
    t -= 1

    while t != 0:
        p += m

        answer += temp[p]
        t -= 1

    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))