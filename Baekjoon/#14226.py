from collections import deque

n = int(input()) # 만들고 싶은 이모티콘 개수

result = [[-1] * 1001 for _ in range(1001)]
result[1][0] = 0 # 초기상태 의미/ 화면에 이모티콘 1개, 클립보드에는 0개

queue = deque()
queue.append((1, 0)) # 화면에 1개, 클립보드 0개

while queue:
    x, clip = queue.popleft()

    if result[x][x] == -1: # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장하는 경우
        result[x][x] = result[x][clip] + 1
        queue.append((x, x))

    if x + clip <= n and result[x + clip][clip] == -1 :# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 하는 경우
        result[x + clip][clip] = result[x][clip] + 1
        queue.append((x + clip, clip))

    if x - 1 >= 0 and result[x - 1][clip] == -1: # 화면에 있는 이모티콘 중 하나를 삭제하는 경우
        result[x - 1][clip] = result[x][clip] + 1
        queue.append((x - 1, clip))

answer = 10000
for i in range(1, n):
    if result[n][i] == -1:
        continue

    else:
        answer = min(answer, result[n][i])

print(answer)