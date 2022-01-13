s = list(input())

stack = []
answer = 0
for i in range(len(s)):
    tmp = s[i]

    if s[i] == '(':
        stack.append('(')

    else:
        if s[i - 1] == '(': # 레이저인 경우
            stack.pop() # 막대기 시작점이라 예상한 부분( ()의 ( 부분 ) 을 제외
            answer += len(stack)

        else:
            stack.pop() # 막대기가 끝났기 때문에 시작부의 '(' 를 제외한다.
            answer += 1

print(answer)