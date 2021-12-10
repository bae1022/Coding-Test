def solution(s):
    answer = ''

    if len(s) % 2 != 0: # 숫자 길이가 홀수라면
        t = len(s) // 2

        answer = s[t]

    elif len(s) % 2 == 0:
        t = len(s) // 2

        answer = s[t - 1 : t + 1]

    return answer

print(solution("abcde"))
print(solution("qwer"))