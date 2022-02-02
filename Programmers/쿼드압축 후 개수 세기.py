def solution(arr):
    answer = [0, 0]  # 0의 개수, 1의 개수

    len_arr = len(arr)

    def quard(x, y, n):
        start = arr[x][y]

        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != start:  # 쿼드 압축 불가능
                    nn = n // 2

                    quard(x, y, nn)
                    quard(x + nn, y, nn)
                    quard(x, y + nn, nn)
                    quard(x + nn, y + nn, nn)
                    return

        answer[start] += 1

    quard(0, 0, len_arr)

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))