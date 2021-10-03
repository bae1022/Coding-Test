from collections import deque

a, b = map(int, input().split())

result = -1

queue = deque()
queue.append((a, 1))

state = 0
while queue:
    temp, cnt = queue.popleft()

    if temp == b:
        state = 1
        result = cnt
        break

    if temp * 2 <= b:
        queue.append((temp * 2, cnt + 1))

    if int(str(temp) + '1') <= b:
        queue.append((int(str(temp) + '1'), cnt + 1))

print(result)