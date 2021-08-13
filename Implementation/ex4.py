# 예제 4
# 문자열 재정렬_ 알파벳 대문자와 숫자로만 구성된 문자열이 입력. 알파벳을 오름차순으로 정렬하여 이어서 출력한 후, 뒤에 숫자를 더한 값을 이어서 출력
# ex) K1KA5CB7 -> ABCKK13

data = input()
result = []
value = 0

for x in data:
    if x.isalpha(): # 알파벳인 경우
        result.append(x)

    else:
        value += int(x)

result.sort()
result.append(str(value))

print(''.join(result)) # 리스트를 문자열로 반환하여 출력함