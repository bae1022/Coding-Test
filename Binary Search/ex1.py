# 예제1
# 떡볶이 떡
# ex 19, 14, 10, 17 길이의 떡이 있을 때, 절단기 높이를 15로 지정하면 4, 0, 0, 2 길이의 떡이 남으며, 손님은 6cm 만큼의 떡을 가져갈 수 있다.
# 손님이 요청한 총 길이가 M일 때 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값

n, m = list(map(int, input().split())) # n은 떡의 개수, m은 손님이 원하는 떡의 길이
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0

    mid = (start + end) // 2

    for i in array:
        if i > mid:
            total += i - mid # 잘랐을 때 떡의 양

    if total < m: # 떡이 부족할 때
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)

