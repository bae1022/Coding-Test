from itertools import permutations

n, m = map(int, input().split())

nums = [i for i in range(1, n + 1)]
n_list = list(permutations(nums, m))

for i in range(len(n_list)):
    print(*n_list[i])