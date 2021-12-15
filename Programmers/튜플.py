def solution(s):
    answer = []

    s = s.split('}')
    temp = []

    for i in range(len(s)):
        t = []

        num = ''
        for j in range(len(s[i])):
            if s[i][j].isdigit():
                num += s[i][j]

            elif s[i][j] == ',':
                if num != '':
                    t.append(num)
                    num = ''

        if num != '':
            t.append(num)

        if len(t) != 0:
            temp.append(t)

    temp.sort(key=lambda x:len(x))

    for i in range(len(temp)):
        n = temp[i][0]
        answer.append(int(n))

        for j in range(i + 1, len(temp)):
            temp[j].remove(n)

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))