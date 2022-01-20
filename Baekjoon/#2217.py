n = int(input())

rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

result = []
for i in range(1, n + 1):
    min_tmp = rope[i - 1]
    result.append(min_tmp * i)

print(max(result))