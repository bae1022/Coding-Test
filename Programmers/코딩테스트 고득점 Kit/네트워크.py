def solution(n, computers):
    answer = 1

    def dfs(start, num): # 시작 숫자, 기록 숫자
        if visit[start] != -1:
            return

        visit[start] = num

        for i in range(n):
            if computers[start][i] == 1 and visit[i] == -1:
                if start == i:
                    continue

                else:
                    dfs(i, num)


    visit = [-1] * n
    for v in range(n):
        if visit[v] == -1:
            dfs(v, v)

    visit.sort()
    for i in range(1, len(visit)):
        if visit[i] == -1:
            answer += 1

        else:
            if visit[i] != visit[i - 1]:
                answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))