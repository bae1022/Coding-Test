n = int(input())

n_list = []


n_list = list(map(int, input().split())) # 왼쪽에 키가 큰 사람이 몇명인지의 리스트
result = [0 for i in range(len(n_list))] # 0으로 초기화된 배열

for i in range(len(n_list)):
    cnt = 0

    for j in range(len(n_list)):
        if n_list[i] == cnt and result[j] == 0:
            result[j] = i + 1
            break

        elif result[j] == 0:
            cnt += 1

print(*result)