import sys

input = sys.stdin.readline # 입력 시 시간 단축

n, m = map(int, input().split())

field = []
temp = [[0] * m for _ in range(n)]

virus = []
for i in range (n):
    row = list(map(int, input().split()))
    field.append(row)

    for j in range(m):
        if row[j] == 2:
            virus.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

def spread_virus(x, y): # 바이러스 퍼뜨리기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2 # 바이러스 배치

                spread_virus(nx, ny) # 재귀 수행

def count_safe():
    result = 0

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1

    return result

def solution(cnt):
    global answer

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = field[i][j] # 복사

        for i in range(len(virus)):
            x, y = virus[i][0], virus[i][1]
            spread_virus(x, y)

        answer = max(answer, count_safe())

    else:
        for i in range(n):
            for j in range(m):

                if field[i][j] == 0:
                    field[i][j] = 1 # 울타리 세우기
                    cnt += 1

                    solution(cnt)

                    field[i][j] = 0
                    cnt -= 1

solution(0)
print(answer)