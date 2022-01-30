n = int(input()) # 스위치의 개수
switches = [0] + list(map(int, input().split())) # 스위치 상태들
m = int(input())

for _ in range(m):
    a, b = map(int, input().split()) # 성별, 받은 수

    if a == 1: # 남학생일 경우
        for i in range(1, n + 1):
            if i % b == 0:
                if switches[i] == 1:
                    switches[i] = 0

                elif switches[i] == 0:
                    switches[i] = 1

    elif a == 2: # 여학생일 경우
        cnt = 1

        while True:
            if 1 <= b - cnt < n + 1 and 1 <= b + cnt < n + 1:
                if switches[b - cnt] == switches[b + cnt]:
                    cnt += 1
                    continue

                else:
                    break

            else:
                break

        for i in range(b - cnt + 1, b + cnt):
            if switches[i] == 1:
                switches[i] = 0

            elif switches[i] == 0:
                switches[i] = 1

for i in range(1, n + 1):
    if i // 20 >= 1 and i % 20 == 1:
        print()
        print(switches[i], end=' ')

    else:
        print(switches[i], end=' ')