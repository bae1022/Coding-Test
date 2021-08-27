# 예제 1
# 상하좌우 문제_ 가장 왼쪽 위(1, 1) / 가장 오른쪽 아래 좌표 (N, N)
# 계획서에 맞게 움직일 때 최종 위치 (범위를 벗어나면 수행하지 않음)

n = int(input())

x = 1
y = 1

plans = input().split()

dx = [0, 0, -1, 1] # x축 L, R, U, D
dy = [-1, 1, 0, 0] # y축 L, R, U, D

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x = nx
        y = ny

print(x, y)