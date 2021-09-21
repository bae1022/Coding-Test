n = int(input()) # 크레인의 수
crane = list(map(int, input().split())) # 크레인의 무게 제한

m = int(input()) # 박스의 수
box = list(map(int, input().split())) # 박스의 무게

crane.sort(reverse=True)
box.sort(reverse=True)

result = 0

if max(box) > max(crane):
    result = -1

else:
    while len(box) > 0:
        result += 1

        for c in crane:
            for b in range(len(box)):
                if box[b] <= c:
                    del box[b]
                    break

print(result)