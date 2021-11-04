a, b = map(int, input().split())

#1,000,000,000 보다 작아야함

answer = 0
def dfs(start, end, n):
    global answer

    if len(str(n)) >= 10:
        return answer

    if n > end:
        return answer

    if start <= n <= end:
        answer += 1

    plus_4 = n * 10 + 4
    plus_7 = n * 10 + 7

    dfs(start, end, plus_4)
    dfs(start, end, plus_7)

    return answer

dfs(a, b, 0)
print(answer)