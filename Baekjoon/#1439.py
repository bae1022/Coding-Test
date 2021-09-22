s = str(input())

cnt_one = 0
cnt_zero = 0

if s[0] == '0':
    cnt_zero += 1

else:
    cnt_one += 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == '0':
            cnt_zero += 1

        else:
            cnt_one += 1

print(min(cnt_one, cnt_zero))