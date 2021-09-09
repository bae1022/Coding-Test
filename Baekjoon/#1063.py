k, s, n = map(str, input().split()) # k: 킹의 위치, s: 돌의 위치, n: 움직이는 횟수

moves = [] # 움직임 리스트
for _ in range(int(n)):
    moves.append(str(input()))

dx_s = ord(s[0]) - 64 # 돌의 x
dy_s = int(s[1]) # 돌의 y

dx_k = ord(k[0]) - 64 # 왕의 x
dy_k = int(k[1]) # 왕의 y

dx = [1, -1, 0, 0, 1, -1, 1, -1] # R, L, B, T, RT, LT, RB, LB
dy = [0, 0, -1, 1, 1, 1, -1, -1]

move_types = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

for move in moves:

    for i in range(len(dx)):

        if move == move_types[i]:
            nx = dx_k + dx[i]
            ny = dy_k + dy[i]

            a = i

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    if nx == dx_s and ny == dy_s:

        nx_s = dx_s + dx[a]
        ny_s = dy_s + dy[a]

        if nx_s < 1 or ny_s < 1 or nx_s > 8 or ny_s > 8:
            continue

        dx_s = nx_s
        dy_s = ny_s

    dx_k = nx
    dy_k = ny

print(chr(dx_k + 64), end='')
print(dy_k)
print(chr(dx_s + 64), end='')
print(dy_s)