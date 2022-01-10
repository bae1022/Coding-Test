n = int(input())

for i in range(n):
    s = input()

    stack = []
    state = 0
    for j in range(len(s)):
        if s[j] == '(':
            stack.append(')')

        elif s[j] == ')':
            if len(stack) == 0:
                state = -1
                break

            stack.pop()

    if len(stack) != 0 or state == -1:
        print('NO')

    else:
        print('YES')