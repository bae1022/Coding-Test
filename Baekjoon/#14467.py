from collections import defaultdict

n = int(input())

cow = defaultdict()
answer = 0
for _ in range(n):
    num, where = map(int, input().split())

    if num in cow.keys():
        if cow[num] != where:
            cow[num] = where
            answer += 1

    else:
        cow[num] = where

print(answer)