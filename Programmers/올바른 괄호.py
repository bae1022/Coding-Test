def solution(s):
    answer = True

    q = []

    for i in range(len(s)):
        if s[i] == "(":
            q.append(")")

        elif s[i] == ")":
            if len(q) == 0:
                return False

            if q[-1] == ")":
                q.pop()

            elif q[-1] != ")":
                return False

    if len(q) != 0:
        return False

    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))