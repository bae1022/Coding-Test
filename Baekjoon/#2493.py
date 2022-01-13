n = int(input())

tower = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    t = tower[i]

    while stack and tower[stack[-1]] < t:
        stack.pop()

    if stack:
        answer[i] = stack[-1] + 1

    stack.append(i)

print(*answer)