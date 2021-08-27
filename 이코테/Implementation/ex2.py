# 예제 2
# 시각_ 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우경우의 수를 구함
# EX) 1을 입력했을 때 00시 00분 03초, 00시 13분 30초 등을 세어야 함

n = int(input())

count = 0

for i in range(n + 1): # 시
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k): # 매 시각 안에 '3'이 포함되어 있다면 카운트 즈아
                count += 1

print(count)