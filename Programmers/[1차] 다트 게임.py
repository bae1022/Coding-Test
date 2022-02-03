def solution(dartResult):
    answer = 0

    t = []
    start = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and i != 0:
            if len(dartResult[start:i]) == 1:
                continue

            t.append(dartResult[start:i])
            start = i

    t.append(dartResult[start:])

    prev = 0
    for i in range(len(t)):
        num = ''
        mult = ''
        op = ''

        for j in range(len(t[i])):
            if t[i][j].isdigit():
                num += t[i][j]

            else:
                if mult == '':
                    mult = t[i][j]

                else:
                    op = t[i][j]

        num = int(num)

        if mult == 'S':
            temp = num

        elif mult == 'D':
            temp = num * num

        else:
            temp = num * num * num

        if op == '*':
            temp = temp * 2
            answer += prev

        elif op == '#':
            temp = -(temp)

        answer += temp
        prev = temp

    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))