def solution(s):
    answer = 0

    def check(ss):
        if ss == ss[::-1]:
            return len(ss)

        return 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            tmp = check(s[i:j])

            answer = max(tmp, answer)

    return answer

print(solution("abcdcba")) # 7
print(solution("abacde")) # 3
print(solution("ecdabbcadc")) # 2