def solution(citations):
    answer = 0

    citations.sort()

    nums = [0] * (citations[-1] + 1)

    cnt = 1

    for i in range(len(citations)):

        for j in range(citations[i] + 1):
            nums[j] += cnt

    for i in range(len(nums)):
        if i == 0:
            continue

        else:
            if i <= nums[i]:
                answer = i

    return answer

print(solution([3, 0, 6, 1, 5])) # 3
print(solution([0, 0, 0, 0, 0])) # 0
print(solution([0, 0, 0, 0, 1])) # 1
print(solution([9, 9, 9, 12])) # 4
print(solution([9, 7, 6, 2, 1])) # 3
print(solution([10, 8, 5, 4, 3])) # 4
print(solution([25, 8, 5, 3, 3])) # 3
print(solution([1, 1, 5, 7, 6])) # 3
print(solution([0])) # 0
print(solution([0, 0])) # 0
