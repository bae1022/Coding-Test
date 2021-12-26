def solution(n, k):
    answer = []

    dp = [0] * 21
    dp[1] = 1

    for i in range(2, 21):
        dp[i] = dp[i - 1] * i

    nums = [i for i in range(1, n + 1)]

    while n != 0:
        a = dp[n] // n # 한 사람이 앞에 줄을 섰을 때 경우의 수
        b = k // a # b바퀴
        k %= a # 나머지

        if k == 0:
            answer.append(nums[b - 1])
            del nums[b - 1]

        else:
            answer.append(nums[b])
            del nums[b]

        n -= 1

    return answer

print(solution(3, 5))