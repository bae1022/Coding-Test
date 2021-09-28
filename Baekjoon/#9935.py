import sys

s = str(input())
bomb = str(input())

stack = []

for i in range(len(s)):
    stack.append(s[i])

    if len(stack) >= len(bomb):
        same = True

        for j in range(-1, (-len(bomb)) - 1, -1): # 거꾸로 순회, -1, -2, ...
            if stack[j] != bomb[j]:
                same = False
                break

        if same is True:
            length = 0

            while length < len(bomb):
                stack.pop()
                length += 1

if len(stack) == 0:
    print("FRULA")

else:
    print("".join(stack))

