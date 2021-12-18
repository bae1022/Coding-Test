from itertools import permutations

def solution(expression):
    answer = 0

    stack = []
    temp = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp += expression[i]

        else:
            stack.append(temp)
            stack.append(expression[i])

            temp = ''

    if temp != '':
        stack.append(temp)

    op = ['+', '-', '*']
    op = list(permutations(op, 3))

    result = []

    def calculate(op_list, nums):
        nn = nums[:]

        for o in range(len(op_list)):
            cnt = 0
            c = 0

            while True:
                if op_list[c] not in nn:
                    c += 1

                    if c == 3:
                        break

                    else:
                        continue

                if str(nn[cnt]).isdigit():
                    pass

                else:
                    if nn[cnt] == op_list[c] and nn[cnt] == '+':
                        nn[cnt - 1] = int(nn[cnt - 1]) + int(nn[cnt + 1])

                        del nn[cnt]
                        del nn[cnt]

                        cnt = 0

                    elif nn[cnt] == op_list[c] and nn[cnt] == '-':
                        nn[cnt - 1] = int(nn[cnt - 1]) - int(nn[cnt + 1])

                        del nn[cnt]
                        del nn[cnt]

                        cnt = 0

                    elif nn[cnt] == op_list[c] and nn[cnt] == '*':
                        nn[cnt - 1] = int(nn[cnt - 1]) * int(nn[cnt + 1])

                        del nn[cnt]
                        del nn[cnt]

                        cnt = 0

                cnt += 1

            return nn[0]

    for i in range(len(op)):
        result.append(abs(calculate(op[i], stack)))

    answer = max(result)

    return answer

print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300
