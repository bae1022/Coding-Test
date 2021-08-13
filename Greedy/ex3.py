# 예제 3_3
# 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 숫자를 확인하며 곱하기 혹은 더하기 연산자를 넣어 만들어질 수 있는 가장 큰 수를 구함
# EX) 02984 문자열이 주어졌을 때, ((((0+2)*9)*8)*4) = 576

data = input()

result = int(data[0]) #첫번째 문자를 숫자로 변경함 (20 -> 2에 해당)

for i in range(1, len(data)): # 256일 경우 5, 6에 해당
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)