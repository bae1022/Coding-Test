n = int(input())

coin_list = list(map(int, input().split()))
coin_list.sort()

target = 1

for coin in coin_list:
    if target < coin:
        break

    target = target + coin

print(target)