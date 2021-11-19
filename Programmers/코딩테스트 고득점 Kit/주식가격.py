def solution(prices):
    answer = []

    for i in range(len(prices)):
        t = prices[i]

        for j in range(i + 1, len(prices)):
            if t > prices[j]:
                break

        answer.append(j - i)

    return answer

print(solution([1, 2, 3, 2, 3]))