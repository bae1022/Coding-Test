def find_pair_index(p):
    cnt_start = 0
    cnt_end = 0

    for i in range(len(p)):
        if p[i] == "(":
            cnt_start += 1

        elif p[i] == ")":
            cnt_end += 1

        if cnt_start == cnt_end:
            break

    return i

def check(p):
    count = 0

    for i in range(len(p)):
        if p[i] == '(':
            count += 1

        else:
            if count == 0:
                return False

            count -= 1

    return True

def solution(p):
    answer = ''

    if p == '':
        return answer

    else:
        index = find_pair_index(p)

        u = p[:index + 1]
        v = p[index + 1:]

        if check(u):
            answer = u + solution(v)

        else:
            answer = '('
            answer += solution(v)
            answer += ')'

            u = list(u[1:-1])

            for i in range(len(u)):
                if u[i] == '(':
                    u[i] = ')'

                elif u[i] == ')':
                    u[i] = '('

                answer += u[i]

    return answer

print(solution('()))((()'))