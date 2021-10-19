n = int(input())

p = []

x = []
y = []

min_l = 10000
max_l = -1
max_h_index = -1
max_h_val = -1

for _ in range(n):
    l, h = map(int, input().split())
    p.append((l, h))

    if l < min_l:
        min_l = l

    if l > max_l:
        max_l = l

    if h > max_h_val:
        max_h_val = h
        max_h_index = l

p_h_list = [0] * (max_l + 1)
for l, h in p:
    p_h_list[l] = h

temp = 0
total = 0
for i in range(max_h_index + 1):
    if p_h_list[i] > temp:
        temp = p_h_list[i]

    total += temp

temp = 0
for i in range(max_l, max_h_index, -1):
    if p_h_list[i] > temp:
        temp = p_h_list[i]

    total += temp

print(total)