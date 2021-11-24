import heapq


def solution(operations):
    answer = []

    h = []
    for i in range(len(operations)):
        o, n = operations[i].split(" ")

        if o == 'I':
            n = int(n)

            heapq.heappush(h, n)

        elif o == 'D':
            if len(h) == 0:
                continue

            if n == '1':
                h.pop()

            elif n == '-1':
                heapq.heappop(h)

    if len(h) == 0:
        answer = [0, 0]

    else:
        answer.append(max(h))
        answer.append(min(h))
    return answer

print(solution(["I 16","D 1"])) # [0, 0]
print(solution(["I 7","I 5","I -5","D -1"])) # [7, 5]