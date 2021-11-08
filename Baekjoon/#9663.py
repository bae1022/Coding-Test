n = int(input())

board = [0] * n # 인덱스 번호=행, 인덱스 값=열
visit = [0] * n

def check(num):
    for i in range(num):
        if (board[num] == board[i]) or (num - i == abs(board[num] - board[i])):
            # 이미 놓여진 퀸과 같은 열이거나, 대각선 상에 있는지를 확인한다.
            # 행끼리의 차 = 열끼리 차의 절댓값 이면 대각선 상에 존재

            return False

    return True

cnt = 0

def sol(num):
    global cnt

    if num == n: # 마지막까지 탐색
        cnt += 1

    else:
        for i in range(n):
            if visit[i] == 1:
                continue

            else:
                board[num] = i # (n, i)에 퀸을 놓는다.

                if check(num) is True:
                    visit[i] = True

                    sol(num + 1)

                    visit[i] = False

sol(0)
print(cnt)