n, l = map(int, input().split())

sign = []

time = 0
temp = 0 # 현재위치

for i in range(n):
    d, r, g = map(int, input().split())

    time += d - temp # 신호등 전까지
    temp = d # 현재위치 갱신

    red = time % (r + g)

    if red <= r:
        time += r - red

time += l - temp
print(time)