from collections import deque

n, k = map(int, input().split()) # n: 수빈이가 있는 위치/ k: 동생이 있는 위치

result = [0] * 100001
def solution(x):

    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()

        if x == k:
            print(result[x])
            break

        else:
            for i in (x - 1, x + 1, x * 2):
                if i >= 0 and i <= 100000 and result[i] == 0:
                    result[i] = result[x] + 1
                    queue.append(i)

if n == k:
    print(0)

else:
    solution(n)

