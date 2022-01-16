from collections import defaultdict

n, m = map(int, input().split()) # n: dna 개수, m: dna 길이

dna = []
for i in range(n):
    dna.append(input())

answer_name = ''
answer_n = 0

i = 0
cnt = 0
dic = defaultdict(lambda: 0)
state = -1
while True:
    if state == 0:
        break

    dic[dna[i][cnt]] += 1

    if i == n - 1:
        if cnt == m - 1:
            state = 0
        t = max(dic.values())

        tmp = []
        for key, value in dic.items():
            if value == t:
                tmp.append(key)

        tmp.sort()

        answer_name += tmp[0]
        answer_n += abs(n - t)

        cnt += 1
        i = 0
        dic.clear()

        continue

    i += 1

print(answer_name)
print(answer_n)