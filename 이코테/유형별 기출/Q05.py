import itertools

n, m = map(int, input().split()) # n: 볼링공의 개수/m: 공의 최대 무게

weight_list = list(map(int, input().split()))

# 조합 라이브러리를 쓰지 않고 해결하는 방법
def x_itertools(n, m, weight_list):
    array = [0] * 11

    for x in weight_list:
        array[x] += 1

    result = 0
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n

    return result

result = list(itertools.combinations(weight_list, 2))

cnt = 0
for i in range(len(result)):
    if result[i][0] == result[i][1]:
        continue
    else:
        cnt += 1

print(cnt)
print(x_itertools(n, m, weight_list))

