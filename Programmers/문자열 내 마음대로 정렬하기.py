def solution(strings, n):
    answer = []

    tmp = []
    for string in strings:
        tmp.append((string[n], string))

    tmp.sort(key=lambda x:(x[0], x[1]))

    for i in range(len(tmp)):
        answer.append(tmp[i][1])

    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
