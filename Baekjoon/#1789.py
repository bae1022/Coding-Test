s = int(input())

i = 1
result = 0
cnt = 0
while(True):
    result += i

    if s - result <= i:
        cnt += 1
        break

    i += 1
    cnt += 1

print(cnt)

# 참고 - n * (n + 1 / 2 : 1부터 n 까지 합의 공식