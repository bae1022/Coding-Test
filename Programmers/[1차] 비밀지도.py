def solution(n, arr1, arr2):
    answer = []

    def to_binary(num):
        result = ''

        while num > 0:
            result += str(num % 2)

            num //= 2

        result = result[::-1]

        if len(result) < n:
            result = ('0' * (n - len(result))) + result

        return result

    for i in range(n):
        temp_a = arr1[i]
        temp_b = arr2[i]

        a = to_binary(temp_a)
        b = to_binary(temp_b)

        temp = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                temp += '#'

            else:
                temp += ' '

        answer.append(temp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], 	[27 ,56, 19, 14, 14, 10]))