def solution(n, lost, reserve):
    answer = 0

    stu = [1] * n

    for i in range(len(lost)):
        num = lost[i] - 1

        stu[num] -= 1

    for i in range(len(reserve)):
        num = reserve[i] - 1

        stu[num] += 1

    for i in range(n):
        if stu[i] == 0: # 체육복이 없는 학생 발견
            for j in range(2):
                if 0 <= (i - 1) < n:
                    if stu[i - 1] == 2:
                        stu[i] += 1
                        stu[i - 1] -= 1
                        break

                if 0 <= (i + 1) < n:
                    if stu[i + 1] == 2:
                        stu[i] += 1
                        stu[i + 1] -= 1
                        break

    for i in range(n):
        if stu[i] >= 1:
            answer += 1


    return answer

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
