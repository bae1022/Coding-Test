import math

def solution(n):
    answer = 0

    temp = ''
    while True:
        if n % 3 == 0 and n // 3 == 0:
            break

        else:
            temp += str(n % 3)
            n //= 3

    temp = temp[::-1]

    for i in range(len(temp)):
        answer += int(temp[i]) * math.pow(3, i)

    return int(answer)

print(solution(45))
print(solution(125))