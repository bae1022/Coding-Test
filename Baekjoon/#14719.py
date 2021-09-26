h, w = map(int, input().split()) # h: 세로길이/ w: 가로길이

blocks = list(map(int, input().split()))

max_h = max(blocks) # 제일 높은 기둥
max_h_index = blocks.index(max_h) # 제일 높은 기둥의 인덱스

answer = 0
start = blocks[0]

temp = 0
total = 0
for i in range(max_h_index + 1):
    if blocks[i] > temp:
        temp = blocks[i]

    total += temp

temp = 0
for i in range(w - 1, max_h_index, -1):
    if blocks[i] > temp:
        temp = blocks[i]

    total += temp

answer = total - sum(blocks)

print(answer)