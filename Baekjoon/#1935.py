n = int(input())
s = list(input())

cnt = 0

dict = {}
nn = 65
for i in range(n):
    t = int(input())
    dict[chr(nn)] = str(t)

    nn += 1

for i in range(len(s)):
    tt = s[i]
    if tt.isalpha():
        s[i] = dict[tt]

stack = []
for i in range(len(s)):
    if s[i].isdigit():
        stack.append(int(s[i]))

    else:
        op = s[i]

        b = stack.pop()
        a = stack.pop()

        if op == '+':
            tmp = a + b

        elif op == '-':
            tmp = a - b

        elif op == '*':
            tmp = a * b

        elif op == '/':
            tmp = a / b

        stack.append(tmp)

print("%.2f"%stack.pop())