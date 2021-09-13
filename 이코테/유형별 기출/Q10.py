def rotate_a_matrix_by_90_degree(a):  # 90도 회전
    n = len(a)  # 행
    m = len(a[0])  # 열

    result = [[0] * n for _ in range(m)]  # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


def check(new_lock):  # 자물쇠와 키를 합하였을 때, 그 배열의 값이 모두 1임을 확인한다.
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False

    return True


def solution(key, lock):  # key: 열쇠를 나타내는 2차원 배열/lock: 자물쇠를 나타내는 2차원 배열
    answer = False

    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]  # 열쇠는 이동 또한 가능하다. 때문에 한 칸씩 이동하며 확인시키기 위하여 크기를 3배로 불린다.

    for i in range(n):  # 3배로 불린 자물쇠 안에 기존의 자물쇠 값을 넣음
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):  # 90도씩 360도가 될 때까지 4번 회전
        key = rotate_a_matrix_by_90_degree(key)

        for x in range(n * 2):  # 한 칸씩 이동하면서 맞춰본다.
            for y in range(n * 2):

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True:
                    answer = True
                    return answer

                else:
                    for i in range(m):  # 자물쇠가 맞지 않는다면 더했던 값을 다시 빼줌으로써 원래 자물쇠 상태로 만듦
                        for j in range(m):
                            new_lock[x + i][y + j] -= key[i][j]

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))