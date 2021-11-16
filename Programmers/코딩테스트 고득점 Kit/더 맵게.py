import heapq

def solution(scoville, K):
    answer = 0

    heap = []

    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])

    if len(scoville) == 1:
        answer = -1

    else:
        while True:
            a = heapq.heappop(heap)

            if len(heap) == 0:
                if a < K:
                    answer = -1
                break

            if a >= K:
                break

            else:
                b = heapq.heappop(heap)

                if a == 0 or b == 0:
                    answer = -1
                    break

                temp = a + (b * 2)

                heapq.heappush(heap, temp)
                answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([8, 10, 11], 7))