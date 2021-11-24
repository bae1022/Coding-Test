import heapq

def solution(jobs):

    h = []

    cnt = 0 # 현재 시간
    temp = 0

    jobs.sort(key=lambda x:x[0])

    index = 1
    cnt = jobs[0][0]
    heapq.heappush(h, (jobs[0][1], jobs[0][0]))
    t = 0

    while True:
        for i in range(index, len(jobs)):
            if jobs[i][0] <= cnt:
                heapq.heappush(h, (jobs[i][1], jobs[i][0])) # 소요시간, 시작시간 삽입
                t = i

        index = t + 1

        if index == len(jobs) and len(h) == 0:
            break

        if index < len(jobs) and len(h) == 0: # 힙은 비어있고 작업을 다 처리하지 못했음
            cnt += 1
            continue

        else:
            time, start = heapq.heappop(h)
            cnt += time
            temp += (cnt - start)

    answer = temp // len(jobs)
    return answer

print(solution([[0, 3], [1, 9], [2, 6]])) # 9
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])) # 74
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])) # 72
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]])) # 7