from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리에 올라갈 수 있는 트럭 수, 다리가 견딜 수 있는 무게, 트럭 별 무게
    answer = 1

    bridge = deque()

    bridge.appendleft((truck_weights[0], bridge_length, 0))

    while True:
        sum_truck = 0
        answer += 1

        for i in range(len(bridge)):
            w, cnt, index = bridge.popleft()
            sum_truck += w

            cnt -= 1

            if cnt == 0:
                sum_truck -= w

            else:
                bridge.append((w, cnt, index))

        if index + 1 == len(truck_weights):
            answer += cnt
            break

        else:
            if len(bridge) < bridge_length and sum_truck + truck_weights[index + 1] <= weight:
                bridge.append((truck_weights[index + 1], bridge_length, index + 1))

    return answer

print(solution(2, 10, [7,4,5,6])) # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]	)) # 110