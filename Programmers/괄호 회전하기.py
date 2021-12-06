def solution(s):
    answer = 0

    def rotate(ss): # 문자열을 왼쪽으로 돌림
        temp = ss[1:]
        temp += ss[0]

        return temp

    def check(ss):
        stack = []
        state = 1

        for j in range(len(ss)):
            if ss[j] == '[':
                stack.append(']')

            elif ss[j] == '{':
                stack.append('}')

            elif ss[j] == '(':
                stack.append(')')

            else:
                if len(stack) == 0:
                    state = 0
                    break

                if len(stack) != 0:
                    if ss[j] != stack[-1]:
                        state = 0
                        break

                    else:
                        stack.pop()

        if state == 0 or len(stack) != 0:
            return 0

        return 1

    for i in range(len(s)):
        s = rotate(s)
        answer += check(s)

    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))