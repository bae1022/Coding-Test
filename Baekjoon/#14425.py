n, m = map(int, input().split())

s = dict()
answer = 0
for i in range(n):
    idx = input()
    s[idx] = True

for i in range(m):
    tmp = input()

    if tmp in s:
        answer += 1

print(answer)
