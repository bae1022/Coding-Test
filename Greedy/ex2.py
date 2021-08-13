# 예제 3_2
# 1이 될때까지_ 과정을 수행해야 하는 횟수의 최솟값 출력

n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k  # n이 k로 나누어 떨어지는 값을 구함
    result += (n - target)
    n = target

    if n < k: # n이 k보다 작을 때 반복문 탈출
        break

    result += 1
    n //= k

result += (n - 1) # 마지막으로 남은 수에 대하여 1씩 빼기
print(result)