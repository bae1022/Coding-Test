def solution(board, moves):
    answer = 0

    stack = []

    for k in range(len(moves)):
        move = moves[k] - 1

        for i in range(len(board)):
            if board[i][move] != 0:
                stack.append(board[i][move])
                board[i][move] = 0
                break

        if len(stack) >= 2:
            a = stack[-1]
            b = stack[-2]

            if a == b:
                stack.pop()
                stack.pop()

                answer += 2

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))