def solution(name):
    answer = 0

    change = []
    for i in range(len(name)):
        c = name[i]

        change.append(min(ord(c) - ord("A"), ord("Z") - ord(c) + 1))

    index = 0

    while True:
        answer += change[index]
        change[index] = 0

        if sum(change) == 0: # 다 바뀌었음
            break

        left = 1
        right = 1

        while change[index - left] == 0:
            left += 1

        while change[index + right] == 0:
            right += 1


        if left < right:
            answer += left
            index += -left

        else:
            answer += right
            index += right

    return answer

print(solution("JEROEN"))
print(solution("JAN"))