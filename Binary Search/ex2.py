# 예제 2
# 정렬된 배열에서 특정 수의 개수 구하기
# N개의 원소 포함하고 있는 수열 오름차순 정렬되어 있음. 수열에서 x가 등장하는 횟수 구하시오

from bisect import bisect_left, bisect_right

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

a = bisect_left(array, m)
b = bisect_right(array, m)

if (b - a == 0):
    print(-1)
else:
    print(b - a)