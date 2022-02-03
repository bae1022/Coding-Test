def solution(price, money, count):
    answer = -1

    pay = 0
    for i in range(1, count + 1):
        pay += (price * (i))

    if money >= pay:
        answer = 0

    else:
        answer = -(money - pay)

    return answer

print(solution(3, 20, 4))