def solution(people, limit):
    answer = 0

    l = []

    for i in range(len(people)):
        l.append(people[i])

    l.sort()

    left = 0
    right = len(people) - 1
    while left <= right:
        a = l[left]
        b = l[right]

        if a + b <= limit:
            left += 1
            right -= 1

            answer += 1

        else:
            right -= 1
            answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))