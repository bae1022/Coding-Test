from collections import deque

n = int(input())

candy = []
for _ in range(n):
    candy.append(list(map(str, input())))

def max_candy(array): # 최대로 먹을 수 있는 사탕을 구한다.

    max_width = 0
    max_height = 0

    cnt1 = 1
    # 행 검사
    for i in range(n):
        cnt1 = 1
        for j in range(1, n):
           if array[i][j] == array[i][j - 1]:

               cnt1 += 1
               max_width = max(max_width, cnt1)

           else:
               cnt1 = 1

    cnt2 = 1
    # 열 검사
    for j in range(n):
        cnt2 = 1
        for i in range(1, n):

            if array[i][j] == array[i - 1][j]:

                cnt2 += 1
                max_height = max(max_height, cnt2)

            else:
                cnt2 = 1

    return max(max_height, max_width)

result = -1

dx = [0, 1]
dy = [1, 0]

result = -1
for i in range(n):
    for j in range(n):
        for k in range(2):

            temp1 = 0
            temp2 = 0

            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            else:
                if candy[i][j] != candy[nx][ny]:
                    candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]

                    temp = max_candy(candy)

                    result = max(temp, result)

                    candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]

print(result)

