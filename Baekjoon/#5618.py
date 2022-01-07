import math

n = int(input())
answer = []

n_list = list(map(int, input().split()))

def gcd(arr): # 최대공약수를 구함
    g = arr[0]

    for item in arr:
        g = math.gcd(g, item)

    return g

limit = gcd(n_list)

for i in range(1, limit + 1):
    for nn in n_list:
        if nn % i == 0:
            state = 0

        else:
            state = -1
            break

    if state != -1:
        answer.append(i)

print(*answer, sep='\n')


