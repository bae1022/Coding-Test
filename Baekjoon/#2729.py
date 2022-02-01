n = int(input())

for _ in range(n):
    a, b = map(str, input().split())

    len_a = len(a)
    len_b = len(b)

    if len_a > len_b:
        b = '0' * (len_a - len_b) + b

    elif len_b > len_a:
        a = '0' * (len_b - len_a) + a

    len_a = len(a) # 갱신
    answer = [0] * (len_a + 1)

    up = 0
    for i in range(-1, -len_a - 1, -1):
        temp = int(a[i]) + int(b[i]) + up

        if temp == 0:
            up = 0
            answer[i] = 0

        elif temp == 1:
            up = 0
            answer[i] = 1

        elif temp == 2:
            up = 1
            answer[i] = 0

        elif temp == 3:
            up = 1
            answer[i] = 1

    if up != 0:
        answer[0] = 1

    result = ''
    for i in range(len(answer)):
        result += str(answer[i])

    result = int(result)
    print(result)