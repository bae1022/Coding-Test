answer = 0
temp = 0

def solution(n):

    def dfs(num, cnt):
        global answer
        global temp

        if num > n:
            return

        if num == n:
            answer += 1
            return

        else:
            temp = num + cnt + 1
            dfs(temp, cnt + 1)

    for i in range(1, n + 1):
        temp = 0
        dfs(i, i)

    return answer

print(solution(15))