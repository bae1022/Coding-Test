from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pocketmon = defaultdict()
pocketmon_num = defaultdict()

cnt = 1
for _ in range(n):
    s = input().rstrip()

    pocketmon[s] = cnt
    pocketmon_num[cnt] = s
    cnt += 1

for _ in range(m):
    s = input().rstrip()

    if s.isdigit(): # 숫자일 경우
        s = int(s)

        print(pocketmon_num[s])

    else:
        print(pocketmon[s])