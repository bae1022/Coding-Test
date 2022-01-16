from itertools import permutations

n = int(input())
k = int(input())

nums = []
for i in range(n):
    nums.append(input())

l = list(permutations(nums, k))

tmp = []

for i in range(len(l)):
    t = list(l[i])
    tmp.append(''.join(t))

tmp = set(tmp)
print(len(tmp))