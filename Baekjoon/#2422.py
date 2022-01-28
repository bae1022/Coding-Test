from itertools import combinations

n, m = map(int, input().split()) # n : 아이스크림의 종류, m: 섞어 먹으면 안 되는 조합의 개ㅜㅅ
ice_cream = [i for i in range(1, n + 1)]

mix_x = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())

    mix_x[a][b] = True
    mix_x[b][a] = True

answer = 0

l = list(combinations(ice_cream, 3))

for li in l:
    a, b, c = li

    if mix_x[a][b] or mix_x[a][c] or mix_x[b][c]:
        continue

    else:
        answer += 1

print(answer)