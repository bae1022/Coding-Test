from collections import deque

def solution(progresses, speeds):
    answer = []

    temp = deque()

    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]

        if (100 - progress) % speed == 0:
            temp.append((100 - progress) // speed)

        elif (100 - progress) % speed != 0:
            temp.append((100 - progress) // speed + 1)

        else:
            temp.append(0)
    print(temp)
    start = temp.popleft()
    cnt = 1
    while temp:
        t = temp.popleft()

        if start >= t:
            cnt += 1

        else:
            answer.append(cnt)
            cnt = 1

            start = t

    if cnt > 0:
        answer.append(cnt)

    return answer

print(solution([5, 5, 5], [21, 25, 20]))