from collections import defaultdict

def solution(n, results):
    answer = 0

    win = defaultdict(set)
    lose = defaultdict(set)

    for i in range(len(results)):
        winner, loser = results[i]

        win[winner].add(loser)
        lose[loser].add(winner)

    for i in range(1, n + 1):
        for winner in lose[i]: # i가 진 사람들은 i가 이긴 사람들 또한 이긴다.
            win[winner].update(win[i])

        for loser in win[i]: # i에게 진 사람들은 i가 진 사람들에게도 진다.
            lose[loser].update(lose[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1: # 이긴 사람 수와 진 사람 수의 합이 전체 인원 - 1(본인) 이면 등수를 알 수 있다.
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # 2