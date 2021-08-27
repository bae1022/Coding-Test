n = int(input())
nums = list(map(int, input().split()))

result = max(nums) * min(nums)

print(result)