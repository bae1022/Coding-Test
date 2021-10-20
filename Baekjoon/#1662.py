
s = str(input())

stack = []
for i in range(len(s)):
    if s[i] != ')':
        stack.append(s[i])

    else:
        cnt = 0

        while stack[-1] != '(':
            output = stack.pop()

            if output == '*':
                length = int(stack.pop())
                cnt += length

            else:
                cnt += 1

        stack.pop()
        length = int(stack.pop())
        cnt *= length

        stack.append(str(cnt))
        stack.append('*')

answer = 0
while stack:
    if stack[-1] == '*':
        stack.pop()
        answer += int(stack.pop())

    else:
        stack.pop()
        answer += 1

print(answer)