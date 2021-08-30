# 예제 3
# 효율적인 화폐 구성_ N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 하여 그 가치의 합이 M원이 되도록
# ex. 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수

n, m = map(int, input().split()) # n은 화폐 단위의 갯수, m은 돈

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1) # 0원부터 m 원까지 각 금액에 대한 최솟값을 확인해야 함

d[0] = 0

# 각 금액에 대한 optimal solution 값을 갱신
for i in range(n): # i는 각각 화폐 단위
    for j in range(array[i], m + 1): # j는 각각 금액을 의미
        if d[j - array[i]] != 10001: # 방법이 존재하는 경우 / 현재 금액에서 확인하고 있는 단위를 뺀 금액을 만들 수 있는 방법이 존재한다면
            d[j] = min(d[j], d[j - array[i]] + 1)


if d[m] == 10001: # m원을 만드는 방법이 없는 경우
    print(-1)

else:
    print(d[m])