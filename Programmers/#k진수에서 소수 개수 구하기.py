import math


def solution(n, k):
    answer = 0

    def prime(x):
        x = int(x)

        if x == 1:
            return False

        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False

        return True

    def convert(n, k):
        tmp = ''

        while n:
            tmp += str(n % k)

            n //= k

        return tmp

    conv = convert(n, k)
    conv = conv[::-1]

    li = conv.split('0')

    for i in range(len(li)):
        if li[i] == '':
            continue

        else:
            if prime(li[i]):
                answer += 1

    return answer

print(solution(437674, 3))
print(solution(110011, 10))