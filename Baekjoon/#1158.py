from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])

cnt = 0
answer = []

while queue:
    x = queue.popleft()
    cnt += 1

    if cnt != k:
        queue.append(x)

    elif cnt == k:
        answer.append(x)
        cnt = 0

print('<', end='')
for i in range(len(answer)):
    if i != len(answer) - 1:
        print(answer[i], end=', ')

    else:
        print(answer[i], end='>')

