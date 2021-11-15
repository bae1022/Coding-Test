answer = 0
def solution(numbers, target):

    def dfs(n, numbers, depth):
        global answer

        if depth == len(numbers):
            if n == target:
                answer += 1

            return

        dfs(n + numbers[depth], numbers, depth + 1)
        dfs(n - numbers[depth], numbers, depth + 1)

    dfs(0, numbers, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))