def solution(lottos, win_nums):
    answer = []

    cnt = 0
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
                continue

    low = cnt  # 최저순위의 맞춘 번호 개수
    high = cnt + lottos.count(0)  # 최고순위의 맞춘 번호 개수

    if 7 - low >= 6:
        low = 6

    else:
        low = 7 - low

    if 7 - high >= 6:
        high = 6

    else:
        high = 7 - high

    answer.append(high)
    answer.append(low)
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))