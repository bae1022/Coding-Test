import math

def solution(arr):
    answer = arr[0]

    for i in range(len(arr)):
        answer = (arr[i] * answer) // math.gcd(arr[i], answer)

    return answer

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))