# 예제 5 _ ☆
# 병사 배치하기_ 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치/ 특정한 위치에 있는 병사를 열외시킬 수 있으나, 남아 있는 병사의 수가 최대로 하도록

# LIS 알고리즘/ 가장 긴 감소하는 부분 수열을 찾는 문제로 변경 가능
n = int(input()) # 병사의 수

attack = list(map(int, input().split()))
attack.reverse() # 순서를 뒤집어 최장 증가 부분 수열 문제로 변환한다.

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if attack[j] < attack[i]: # 앞에 있는 원소가 자신보다 작은 경우에 한해서
            dp[i] = max(dp[i], dp[j] + 1) # 테이블 갱신

print(n - max(dp)) # 열외해야 하는 병사의 최소 수 출력