# 예제 3_4
# 모험가 길드
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다. 여행을 떠날 수 있는 그룹 수의 최댓값

n = int(input()) # 모험가 수
data = list(map(int, input().split())) # 각 모험가의 공포도
data.sort() # 오름차순으로 정렬

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1

    if count >= i:
        result += 1
        count = 0

print(result)