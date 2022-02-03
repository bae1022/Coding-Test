def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue

        t = ord(s[i])
        temp = ord(s[i]) + n

        if 97 <= t <= 122:  # 소문자임
            if temp > 122:
                temp -= 26

            answer += chr(temp)

        elif 65 <= t <= 90:  # 대문자임
            if temp > 90:
                temp -= 26

            answer += chr(temp)

    return answer

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))