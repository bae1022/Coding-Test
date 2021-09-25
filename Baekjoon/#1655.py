import heapq
from sys import stdin

n = int(stdin.readline())

left = [] # 최대 힙
right = [] # 최소 힙

for _ in range(n):
    num = int(stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -num) # heapq는 최소힙만 지원/ 최대힙으로 만들기 위해서 - 를 곱해주는 것.

    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]: # right에 원소가 있으면서, 왼쪽 값이 오른쪽 값보다 큰 경우 (left보다 right 가 커야하는 조건에 위배)
        left_value = heapq.heappop(left)
        right_value = heapq.heappop(right)

        heapq.heappush(left, -right_value)
        heapq.heappush(right, -left_value)

    print(-left[0])

