import heapq

def solution(n, works):
    answer = 0

    h = []
    for i in range(len(works)):
        heapq.heappush(h, (-works[i], works[i]))

    while n != 0:
        t = heapq.heappop(h)[1]
        t2 = t - 1

        if t2 < 0:
            break

        else:
            heapq.heappush(h, (-t2, t2))
            n -= 1

    while h:
        tmp = heapq.heappop(h)[1]

        answer += (tmp**2)

    return answer

print(solution(4, [4, 3, 3])) # 12
print(solution(1, [2, 1, 2])) # 6
print(solution(3, [1, 1]))# 0