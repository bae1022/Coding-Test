from collections import defaultdict

n, m = map(int, input().split())

words = defaultdict()
answer = []
cnt = 0

for i in range(n):
    s = input()

    words[s] = 1

for i in range(m):
    s = input()

    if s in words.keys():
        cnt += 1
        answer.append(s)

answer.sort()

print(cnt)
print('\n'.join(answer))

