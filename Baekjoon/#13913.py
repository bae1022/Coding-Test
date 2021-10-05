from collections import deque

n, k = map(int, input().split())

result = [0] * 100001
visit = [0] * 100001
move = [0] * 100001

def solution(n):
    queue = deque()
    queue.append(n)

    visit[n] = 1
    result[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            break

        for i in (x - 1, x + 1, x * 2):
            if i >= 0 and i <= 100000:
                if visit[i] == 0:
                    result[i] = result[x] + 1
                    visit[i] = visit[x]

                    queue.append(i)
                    move[i] = x # 부모 노드를 담는다.

solution(n)
print(result[k])

temp = k
path = []
for i in range(result[k] + 1):
    path.append(temp)

    temp = move[temp] # 부모를 계속 타고 올라가 path 배열에 담는다.

print(*path[::-1]) # 대괄호 제외하고 반대로 출력
