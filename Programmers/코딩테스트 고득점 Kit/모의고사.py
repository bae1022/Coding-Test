def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]

    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10

        if p1[s1] == answers[i]:
            cnt[0] += 1

        if p2[s2] == answers[i]:
            cnt[1] += 1

        if p3[s3] == answers[i]:
            cnt[2] += 1

    a = max(cnt)

    for i in range(3):
        if a == cnt[i]:
            answer.append(i + 1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))