from collections import deque

def solution(priorities, location):
    answer = 0

    temp = deque()

    for i in range(len(priorities)):
        temp.append((i, priorities[i]))

    while temp:
        index, j = temp.popleft() # 현재 대기목록의 가장 앞에 있는 문서를 대기목록에서 꺼냄

        if j < max(priorities): # 꺼낸 것보다 중요도가 높은 것이 있다면
            temp.append((index, j)) # 다시 삽입

        else:
            priorities.remove(j)
            answer += 1

            if index == location:
                break

    return answer

print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5