def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(len(A)):
        a = A[i]

        if a >= B[0]:
            continue

        else:
            answer += 1
            del B[0]

    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))
print(solution([2,2,2,2], [2,2,2,2]))