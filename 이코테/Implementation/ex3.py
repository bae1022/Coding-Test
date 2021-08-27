# 예제 3
# 왕실의 나이트_ 8*8 좌표 평면/ 이동할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 이동할 수 없다. 좌표 평면상에서 나이트가 이동할 수 있는 경우의 수 출력
# 나이트는 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동/2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동 만 가능

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #ord: ASCII

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)