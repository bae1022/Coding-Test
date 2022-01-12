from collections import deque

n = int(input())
nums = list(input().split())
balloons = deque()

for i in range(n):
    balloons.append(((i + 1), int(nums[i])))

answer = []

b, num = balloons.popleft()
limit = num
answer.append(b)

cnt = 0
while balloons:
    if limit < 0:
        b, num = balloons.pop()
        cnt -= 1

    elif limit > 0:
        b, num = balloons.popleft()
        cnt += 1

    if cnt == limit:
        cnt = 0
        answer.append(b)
        limit = num

    else:
        if limit < 0:
            balloons.insert(0, (b, num))

        elif limit > 0:
            balloons.append((b, num))

print(*answer)