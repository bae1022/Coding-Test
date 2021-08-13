# 예제 3-1
# 거스름돈_거슬러줘야 할 돈이 1260원일 때, 거슬러주어야 할 동전의 최소 개수
a = [500, 100, 50, 10]

n = 1260
count = 0

for coin in a:
    count += n // coin
    n %= coin

print(count)