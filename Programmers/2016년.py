def solution(a, b):
    answer = ''

    calendar = {1: 31, 2: 29, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    n = a - 1
    t = 0
    for i in range(1, n + 1):
        t += calendar[i]

    t += b

    temp = t % 7

    if temp == 1:
        answer = 'FRI'

    elif temp == 2:
        answer = 'SAT'

    elif temp == 3:
        answer = 'SUN'

    elif temp == 4:
        answer = 'MON'

    elif temp == 5:
        answer = 'TUE'

    elif temp == 6:
        answer = 'WED'

    elif temp == 0:
        answer = 'THU'

    return answer

print(solution(5, 24)) # "TUE"