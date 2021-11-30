def solution(s):
    answer = -1

    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])

        else:
            if s[i] == stack[-1]:
                stack.pop()

            else:
                stack.append(s[i])

    if len(stack) == 0:
        answer = 1

    else:
        answer = 0

    return answer

print(solution("baabaa")) # 1
print(solution("cdcd")) # 0
print(solution("aabbccdd"))