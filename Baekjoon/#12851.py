from collections import deque

n, k = map(int, input().split()) # n: 수빈이가 있는 위치/ k: 동생이 있는 위치

result = [0] * 100001
visit = [0] * 100001

def solution(n):
    queue = deque()
    queue.append(n)

    visit[n] = 1
    result[n] = 0

    while queue:
        x = queue.popleft()

        for i in (x - 1, x + 1, x * 2):
            if i >= 0 and i <= 100000:
                if visit[i] == 0: # 방문한 적이 없음

                    result[i] = result[x] + 1 # 시간 저장

                    visit[i] = visit[x] # 방문 횟수 저장 (dp 방식과 유사)

                    queue.append(i)

                elif result[i] == result[x] + 1 : # 방문한 적 있으며, 최단시간인 경우
                    visit[i] += visit[x] # dp 방식과 유사

if n == k:
    print(0)
    print(1)

else:
    solution(n)
    print(result[k])
    print(visit[k])