n, m = map(int, input().split()) # n, m = 행렬의 크기

map1 = [list(map(int, input())) for _ in range(n)]
map2 = [list(map(int, input())) for _ in range(n)]

def change3_3(start_x, start_y, array): # 3*3 배열만큼 숫자를 바꾼다.

    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            array[i][j] = 1 - array[i][j]

cnt = 0 # 변환 횟수
for i in range(n - 2): # 행렬을 초과하지 않도록 경계를 준다.
    for j in range(m - 2):
        if (map1[i][j] != map2[i][j]):
            change3_3(i, j, map1)
            cnt += 1

state = 1 # -1: 불일치/1: 일치
for i in range(n):
    if map1[i] != map2[i]:
        state = -1
        break

if state != -1:
    print(cnt)
else:
    print(state)