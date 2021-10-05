from collections import deque

n, k = map(int, input().split()) # n: 수빈이의 위치/k: 동생의 위치

result = [0] * 100001
visit = [0] * 100001

def solution(n):
    queue = deque()
    queue.append(n)

    visit[n] = 1
    result[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            break

        else:
            for i in (x - 1, x + 1, x * 2):
                if i >= 0 and i <= 100000 and visit[i] == 0:
                    if i == x * 2:
                        result[i] = result[x]
                        visit[i] = visit[x]

                        queue.appendleft(i) # 순간이동의 경우, 시간소요가 없다. 따라서 popleft로 2*x 가 더 높은 우선순위를 가지도록 한다.

                    else:
                        result[i] = result[x] + 1
                        visit[i] = visit[x]

                        queue.append(i)

solution(n)
print(result[k])