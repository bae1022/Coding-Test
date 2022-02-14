t = int(input())

for _ in range(t):
    keylog = list(input())

    a = []
    b = []
    result = []

    for i in range(len(keylog)):
        if keylog[i] == '<': # a 배열에서 b 배열로 이동
            if len(a) > 0:
                x = a.pop()
                b.append(x)

        elif keylog[i] == '>':
            if len(b) > 0:
                x = b.pop()
                a.append(x)

        elif keylog[i] == '-':
            if len(a) > 0:
                x = a.pop()

        else:
            a.append(keylog[i])

    print(*a, sep='', end='')
    b = b[::-1]
    print(*b, sep='')