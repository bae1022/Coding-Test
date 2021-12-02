def solution(dirs):
    answer = 0

    dx = [0, 0, 1, -1] # U, D, R, L
    dy = [-1, 1, 0, 0]

    x = 0
    y = 0

    record = []
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            nx = x + dx[0]
            ny = y + dy[0]

        elif dirs[i] == 'D':
            nx = x + dx[1]
            ny = y + dy[1]

        elif dirs[i] == 'R':
            nx = x + dx[2]
            ny = y + dy[2]

        elif dirs[i] == 'L':
            nx = x + dx[3]
            ny = y + dy[3]

        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        else:
            temp1 = 'x' + str(x) + 'y' + str(y) + 'nx' + str(nx) + 'ny' + str(ny)
            temp2 = 'x' + str(nx) + 'y' + str(ny) + 'nx' + str(x) + 'ny' + str(y)

            if temp1 in record or temp2 in record:
                pass

            else:
                answer += 1
                record.append(temp1)
                record.append(temp2)

            x = nx
            y = ny

    return answer

print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7