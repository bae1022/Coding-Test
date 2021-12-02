from itertools import combinations
import math

def solution(nums):
    answer = 0

    combi_list = list(combinations(nums, 3))

    def prime_check(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True

    for i in range(len(combi_list)):
        temp = combi_list[i][0] + combi_list[i][1] + combi_list[i][2]

        if prime_check(temp):
            answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))