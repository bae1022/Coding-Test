def solution(numbers, hand):
    answer = ''

    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    left_x, left_y = 3, 0
    right_x, right_y = 3, 2

    for k in range(len(numbers)):
        if numbers[k] == 1 or numbers[k] == 4 or numbers[k] == 7:
            answer += 'L'

            for i in range(4):
                for j in range(3):
                    if pad[i][j] == numbers[k]:
                        left_x, left_y = i, j

        if numbers[k] == 3 or numbers[k] == 6 or numbers[k] == 9:
            answer += 'R'

            for i in range(4):
                for j in range(3):
                    if pad[i][j] == numbers[k]:
                        right_x, right_y = i, j

        if numbers[k] == 2 or numbers[k] == 5 or numbers[k] == 8 or numbers[k] == 0:
            temp_x, temp_y = 0, 0

            for i in range(4):
                for j in range(3):
                    if pad[i][j] == numbers[k]:
                        temp_x, temp_y = i, j

            a1 = temp_x - left_x
            b1 = temp_y - left_y

            a2 = temp_x - right_x
            b2 = temp_y - right_y

            length1 = abs(a1) + abs(b1)
            length2 = abs(a2) + abs(b2)

            if length1 == length2:
                if hand == 'left':
                    answer += 'L'

                    left_x, left_y = temp_x, temp_y

                elif hand == 'right':
                    answer += 'R'

                    right_x, right_y = temp_x, temp_y

            else:
                t = min(length1, length2)

                if t == length1:
                    answer += 'L'
                    left_x, left_y = temp_x, temp_y

                elif t == length2:
                    answer += 'R'
                    right_x, right_y = temp_x, temp_y


    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")) # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 	"right")) # "LLRLLRLLRL"