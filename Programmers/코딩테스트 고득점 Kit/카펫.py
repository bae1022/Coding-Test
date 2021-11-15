def solution(brown, yellow):
    answer = []

    total = brown + yellow # 총 블럭

    for col in range(3, total): # 갈색블럭 -> 테두리, 노란색 블럭 -> 안/ 행은 최소 3개
        row = total / col # 열의 개수

        if (row * col == total) and  (row >= col) and ((col - 2) * (row - 2) == yellow):
            # 행, 열을 곱했을 때 총 블럭의 수가 나와야 하고,
            # 가로 길이가 세로 길이와 같거나, 세로 길이보다 길어야 하고,
            # 열-2 * 행 - 2가 노란 블럭의 수와 같아야 한다.

            answer.append(int(row))
            answer.append(col)

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))