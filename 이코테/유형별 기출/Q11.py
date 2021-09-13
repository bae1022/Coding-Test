n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

field = [[0] * (n + 1) for _ in range(n + 1)]
# field[1][1] = 9 # 뱀은 9로 표현/ 첫번째 위치는 왼쪽 맨위

for _ in range(k):
    x, y = map(int, input().split()) # 사과의 위치
    field[x][y] = 1

move_n = int(input())

snake = []
for _ in range(move_n):
    time, move = map(str, input().split())
    snake.append((int(time), move))

def turn(direction, c): # 방향 전환
    if c == "L": # 왼쪽으로 회전
        direction = (direction - 1) % 4

    else: # 오른쪽으로 회전
        direction = (direction + 1) % 4

    return direction

# 순서대로 동, 서, 남, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
direction = 0 # 0: 동/1: 서/2: 남/3: 북

x = 1
y = 1

field[x][y] = 9  # 뱀 위치 표시
q = [(x, y)] # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽 위치)
index = 0 # 회전 정보

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx >= 1 and nx <= n and ny >= 1 and ny <= n and field[nx][ny] != 9:
        if field[nx][ny] == 0: # 사과가 없는 상태
            field[nx][ny] = 9

            q.append((nx, ny))

            px, py = q.pop(0) # 몸 길이를 줄인다.
            field[px][py] = 0

        if  field[nx][ny] == 1: # 사과가 있는 상태
            field[nx][ny] = 9
            q.append((nx, ny))

    else:
        cnt += 1
        break
    x, y = nx, ny
    cnt += 1

    if index < move_n and cnt == snake[index][0]: # index < move_n 해주지 않으면 index 에러.
        direction = turn(direction, snake[index][1])
        index += 1

print(cnt)

