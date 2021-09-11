import heapq

def solution(food_times, k):  # food_times: 각 음식을 모두 먹는 데 필요한 시간/ k: 방송이 중단된 시간

    if sum(food_times) <= k:
        return -1

    q = []

    print(food_times)
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (음식 시간, 음식 번호)

    sum_value = 0 # 총 시간
    previous = 0 # 몇바퀴 돌았는지
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        print('now', now)

        sum_value += (now - previous) * length
        print('sum_value', sum_value)
        length -= 1
        previous = now
        print('previous', previous)

    result = sorted(q, key =lambda x:x[1])

    print(result)

    answer = result[(k - sum_value) % length][1]

    return answer

print(solution([8, 6, 4], 15))