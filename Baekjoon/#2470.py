n = int(input())

l = list(map(int, input().split()))
l.sort()

left = 0
right = n - 1

answer = 10000000001
result = []

while left < right:
    t1 = l[left]
    t2 = l[right]

    temp = t1 + t2

    if abs(temp) < answer:
        answer = abs(temp)

        result = [t1, t2]

    if temp < 0: # 왼쪽의 값 늘려주기
        left += 1

    else:
        right -= 1

print(result[0], result[1])