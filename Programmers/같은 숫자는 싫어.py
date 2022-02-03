def solution(arr):
    answer = []

    prev = -1
    for i in range(len(arr)):
        if i == 0:
            prev = arr[i]
            answer.append(prev)
            continue

        if prev == arr[i]:
            continue

        else:
            prev = arr[i]
            answer.append(prev)

    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))