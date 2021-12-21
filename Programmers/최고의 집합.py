def solution(n, s):
    answer = []

    if n > s:
        answer = [-1]

    else:
        start = s // n
        r = s % n

        answer = [start] * n

        for i in range(-1, -r - 1, -1):
            answer[i] += 1

    return answer

print(solution(2, 9)) #[4, -5]
print(solution(2, 1)) #[-1]
print(solution(2, 8)) #[4, 4]