answer = 0
def solution(n, money):

    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m] # 기존의 동전 종류를 이용해 n을 만드는 경우의 수 + 새 동전 종류를 사용했을 때의 경우의 수

    return dp[n] % 1000000007

print(solution(5, [1,2,5]))