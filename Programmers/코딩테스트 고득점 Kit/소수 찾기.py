import math
from itertools import permutations

def check(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0

    temp = [] # 조합들을 넣을 배열
    nums = []

    for i in range(len(numbers)):
        nums.append(numbers[i])

    for i in range(1, len(numbers) + 1):
        temp += list(permutations(nums, i))

    new_nums = []
    for i in range(len(temp)):
        t = temp[i]
        tt = ''

        for j in range(len(temp[i])):
            tt += temp[i][j]

        if check(int(tt)):
            if int(tt) < 2:
                continue

            new_nums.append(int(tt))

    answer = len(set(new_nums)) # set으로 중복 제거

    return answer

print(solution("17"))
print(solution("011"))