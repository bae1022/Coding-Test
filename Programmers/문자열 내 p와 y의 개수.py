def solution(s):
    answer = True

    s = s.lower()

    cnt_y = s.count('y')
    cnt_p = s.count('p')

    if cnt_y == cnt_p:
        return True

    else:
        return False

print(solution("pPoooyY"))
print(solution("Pyy"))