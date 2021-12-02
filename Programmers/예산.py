def solution(d, budget):
    answer = 0

    d.sort()

    i = 0
    while True:
        if i >= len(d):
            break

        money = d[i]
        budget -= money

        if budget < 0:
            break

        else:
            i += 1
            answer += 1

    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))