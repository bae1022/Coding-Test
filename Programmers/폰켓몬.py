def solution(nums):
    answer = 0

    pick_n = len(nums) // 2 # 고를 수 있는 폰켓몬의 수

    nums = set(nums)
    n = len(nums) # 동물 종류의 수

    if pick_n >= n:
        answer = n

    elif pick_n < n: # 종류가 더 많은 경우
        answer = pick_n

    return answer

print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2