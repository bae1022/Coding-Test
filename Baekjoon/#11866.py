from collections import deque

n, k = map(int, input().split())

people = deque([i for i in range(1, n + 1)])

print('<', end='')
while people:
    for i in range(k - 1): # 원의 순서를 바꾼다.
        people.append(people[0])
        people.popleft()

    print(people.popleft(), end='')

    if people:
        print(', ', end='')
print('>')