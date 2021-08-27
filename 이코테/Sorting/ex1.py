# 예제 1
# 데이터를 바꿔치기 하여 최댓값 구하기 (N=배열 크기/K=바꿔치기 가능 횟수)

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if (a[i] < b[i]):
        a[i], b[i] = b[i], a[i]

print(sum(a))