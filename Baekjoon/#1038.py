import sys
from itertools import combinations

n = int(input())

nums = []

for i in range(1, 11): # 0 부터 9까지의 숫자/ 10개임
    for comb in combinations(range(0, 10), i): # 0부터 9까지의 숫자 i 개를 이용해서 조합 생성
        comb = list(comb)
        comb.sort(reverse=True)

        nums.append(int("".join(map(str, comb))))

nums.sort()

try:
    print(nums[n])
except: # 인덱스가 넘어가는 경우
    print(-1)