from collections import defaultdict

n = int(input())
files = []

kinds = defaultdict(lambda:0)

for _ in range(n):
    s = input()
    ss = s.split('.')

    kinds[ss[1]] += 1

temp = []
for key, value in kinds.items():
    temp.append((key, value))

temp = sorted(temp, key=lambda x:x[0])

for t in temp:
    a, b = t

    print(a, b)