from collections import deque

n, m = map(int, input().split()) # n: 큐의 크기, m: 뽑아내려고 하는 수의 개수
# n <= 50, m <= n
s = list(map(int, input().split())) # 뽑아내려고 하는 수의 위치 리스트

q = deque([i for i in range(1, n + 1)])

cnt = 0
for i in range(len(s)):
    while True:
        if q[0] == s[i]:
            q.popleft()
            break

        else:
            if q.index(s[i]) < len(q) / 2: # 위치가 앞쪽인 경우, 2번 연산 수행
                while q[0] != s[i]:
                    q.append(q.popleft())
                    cnt += 1

            else: # 원소를 빼서 앞으로 보냄, 3번 연산
                while q[0] != s[i]:
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)