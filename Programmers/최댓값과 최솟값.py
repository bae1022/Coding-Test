def solution(s):
    answer = ''

    s_arr = s.split(' ')
    new_arr = []

    for num in s_arr:
        if num[0] == '-':
            new_arr.append(int(num[1:]) * (-1))

        else:
            new_arr.append(int(num))

    answer += str(min(new_arr))
    answer += ' ' + str(max(new_arr))

    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
