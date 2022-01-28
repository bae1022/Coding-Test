field = [[0] * 19 for _ in range(19)]

for i in range(19):
    col = list(map(int, input().split()))
    for j in range(19):
        field[i][j] = col[j]

dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]

def win(x, y, state, who): # state / 0: 세로방향, 1: 가로방향, 2: 대각선 방향
    cnt = 1

    start_x = x
    start_y = y

    while True:
        nx = x + dx[state]
        ny = y + dy[state]

        if 0 <= nx < 19 and 0 <= ny < 19:
            if field[nx][ny] == who:
                cnt += 1

                x = nx
                y = ny

            else:
                break

        else:
            break

    if cnt == 5:
        if state == 0:
            if 0 <= start_x - 1 < 19 and 0 <= start_y < 19:
                if field[start_x - 1][start_y] == who:
                    return False

                else:
                    return True

            else:
                return True

        elif state == 1:
            if 0 <= start_x < 19 and 0 <= start_y - 1 < 19:
                if field[start_x][start_y - 1] == who:
                    return False

                else:
                    return True

            else:
                return True

        elif state == 2:
            if 0 <= start_x - 1 < 19 and 0 <= start_y - 1 < 19:
                if field[start_x - 1][start_y - 1] == who:
                    return False
                else:
                    return True

            else:
                return True

        elif state == 3:
            if 0 <= start_x + 1 < 19 and 0 <= start_y - 1 < 19:
                if field[start_x + 1][start_y - 1] == who:
                    return False
                else:
                    return True

            else:
                return True

    return False

who_win = 0
answer_x = -1
answer_y = -1

for i in range(19):
    for j in range(19):
        if field[i][j] == 1: # 흰색 바둑알의 경우
            for k in range(4):
                if win(i, j, k, 1):
                    who_win = 1

                    answer_x = i
                    answer_y = j

                    break

                else:
                    continue

        elif field[i][j] == 2:
            for k in range(4):
                if win(i, j, k, 2):
                    who_win = 2

                    answer_x = i
                    answer_y = j

                    break

        else:
            continue

print(who_win)

if who_win != 0:
    print(answer_x + 1, answer_y + 1)
