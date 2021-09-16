import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)

    sum_n = n1 + n2
    result += sum_n

    heapq.heappush(heap, sum_n)

print(result)