import math

def is_prime_number(x): # 소수 판별

    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

n = int(input())

def dfs(num): # 하나하나 비교하면 시간 초과/ dfs로 탐색하며 소수를 찾는다.
    if len(str(num)) == n:
        print(num)

    else:
        for i in range(10):
            temp = num * 10 + i

            if is_prime_number(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)