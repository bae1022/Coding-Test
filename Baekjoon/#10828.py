import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    m = str(sys.stdin.readline())

    a = m.split()

    if a[0] == 'push':
        stack.append(a[1])

    elif a[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif a[0] == 'size':
        print(len(stack))

    elif a[0] == 'empty':
        if len(stack) == 0:
            print(1)

        else:
            print(0)

    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
