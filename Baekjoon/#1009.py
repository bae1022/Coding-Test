import math

num = int(input())

for i in range(num):
    n, m = map(int, input().split())

    n = n % 10

    if n == 0:
        print(10)

    elif n == 1 or n == 5 or n == 6:
        print(n) # 위의 숫자들은 제곱해도 일의자리는 자기 자신이 출력된다.

    elif n == 4 or n == 9: # 4와 9는 사이클의 크기가 2
        m = m % 2

        if m == 1: # 홀수 제곱을 할 경우 자기 자신이 출력
            print(n)
        else: # 짝수 제곱의 경우 각각 6과 1을 출력
            print((n * n) % 10)

    else: # 나머지는 사이클이 4
        m = m % 4

        if m == 0:
            print((n ** 4) % 10)
        else:
            print((n ** m) % 10)
