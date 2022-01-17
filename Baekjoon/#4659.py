
while True:
    s = input()

    if s == 'end':
        break

    cnt = 0 # 모음 개수 세기
    limit = 2
    state = -1 # 0은 모음, 1은 자음

    before = s[0]
    result_state = 0

    if before == 'e' or before == 'a' or before == 'i' or before == 'o' or before == 'u':
        state = 0
        cnt += 1

    else:
        state = 1

    for i in range(1, len(s)):
        if (before == 'e' and s[i] == 'e') or (before == 'o' and s[i] == 'o'):
            pass

        elif before == s[i]:
            result_state = -1
            break

        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            cnt += 1 # 모음의 개수를 증가시킨다.

            if state == 1: # 전 문자가 자음일 때
                limit = 2 # 리셋

            elif state == 0:
                limit -= 1
            state = 0 # 상태가 모음임

        else:
            if state == 0: # 전 문자가 모음일 때
                limit = 2

            elif state == 1:
                limit -=1

            state = 1

        if limit <= 0:
            result_state = -1
            break

        before = s[i]

    if cnt == 0: # 모음 하나를 반드시 포함해야 한다.
        result_state = -1

    if result_state == -1:
        print('<' + s + '>' + ' is not acceptable.')

    else:
        print('<' + s + '>' + ' is acceptable.')
