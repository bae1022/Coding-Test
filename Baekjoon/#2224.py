n = int(input())
arr = [[0] * 58 for _ in range(58)]
cnt = 0

for _ in range(n):
    s = list(map(str, input().split(' => ')))

    if s[0] == s[1]:
        continue

    if arr[ord(s[0]) - 65][ord(s[1]) - 65] == 0:
        arr[ord(s[0]) - 65][ord(s[1]) - 65] = 1
        cnt += 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and arr[i][j] == 0 and arr[i][k] and arr[k][j]:
                arr[i][j] = 1
                cnt += 1

print(cnt)
for i in range(58):
    for j in range(58):
        if arr[i][j] == 1:
            print(chr(i + 65) + ' => ' + chr(j + 65))