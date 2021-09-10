n = int(input()) # 모험가의 수
fear_list = list(map(int, input().split())) # 공포도 나열 배열

fear_list.sort()

result = 0
count = 0

for i in range(n):
    count += 1

    if count >= fear_list[i]:
        result += 1
        count = 0

print(result)