from collections import deque

n, m, t = map(int, input().split()) # t: 제한 시간

castle = [[0] * m for _ in range(n)]

for i in range(n):
    col = list(map(int, input().split()))

    for j in range(m):
        castle[i][j] = col[j]

        if col[j] == 2:
            sword = (i, j) # 검의 위치 기록

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_sword(x, y): # 칼을 찾는 최단시간
    q = deque()
    q.append((x, y, 0))

    visit = [[False] * m for _ in range (n)]
    visit[x][y] = True

    cnt = -1
    while q:
        x, y, time = q.popleft()
        visit[x][y] = True

        if castle[x][y] == 2: # 검이 발견됨
            cnt = time
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and castle[nx][ny] != 1:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny, time + 1))

    return cnt


def from_sword(x, y): # 칼이 있는 위치부터 공주의 위치까지
    q = deque()
    q.append((x, y, 0))

    visit = [[False] * m for _ in range(n)]
    visit[x][y] = True

    cnt = -1
    while q:
        x, y, time = q.popleft()
        visit[x][y] = True

        if x == n - 1 and y == m - 1:
            cnt = time
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 벽 뚫고 갈 수 있기 때문에 제약 X
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny, time + 1))

    return cnt

def no_sword(x, y):
    q = deque()
    q.append((x, y, 0))

    visit = [[False] * m for _ in range(n)]
    visit[x][y] = True

    cnt = -1
    while q:
        x, y, time = q.popleft()
        visit[x][y] = True

        if x == n - 1 and y == m - 1:
            cnt = time
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and castle[nx][ny] == 0:  # 벽 뚫고 갈 수 있기 때문에 제약 X
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny, time + 1))

    return cnt

a = find_sword(0, 0) # 칼을 찾아감
b = no_sword(0, 0) # 칼 없이 길을 찾아감
if a == -1: # 칼을 발견하지 못했음
    if b == -1:
        print('Fail')

    else:
        print(b)

else:
    c = from_sword(sword[0], sword[1]) # 칼에서 출발

    if b == -1: # 칼을 들지 않고서는 갈 수 없는 경우
        temp = a + c

    else:
        temp = min(a + c, b)

    if temp <= t:
        print(temp)

    else:
        print('Fail')