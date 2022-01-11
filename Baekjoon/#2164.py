from collections import deque

n = int(input())

cards = deque([i for i in range(1, n + 1)])

cnt = 0
while cards:
    c = cards.popleft()

    if cnt == 0:
        cnt += 1

    else:
        cards.append(c)
        cnt = 0

print(c)