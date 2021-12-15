def solution(s):
    answer = ''

    s_arr = s.split(' ')

    for i in range(len(s_arr)):
        t1 = s_arr[i][:1].upper()
        t2 = s_arr[i][1:].lower()

        s_arr[i] = t1 + t2

    return ' '.join(s_arr)

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("333   aaa"))
print(solution("aaaaa aaa"))