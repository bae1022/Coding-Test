from collections import deque

n, m = map(int, input().split())
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

answer = []
while a and b:
    t1 = a.popleft()
    t2 = b.popleft()

    if t1 > t2:
        answer.append(t2)
        a.appendleft(t1)

    elif t1 <= t2:
        answer.append(t1)
        b.appendleft(t2)

if len(a) != 0:
    answer = answer + list(a)

elif len(b) != 0:
    answer = answer + list(b)

print(*answer)

