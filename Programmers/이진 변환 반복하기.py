def solution(s):
    def remove_zero(num):
        cnt = num.count('0')
        num = num.replace('0', '')

        return cnt, num

    def to_binary(num):
        result = []

        while num != 0:
            result.append(str(num % 2))
            num //= 2

        return result[::-1]

    count_zero = 0
    count_binary = 0
    while s != '1':
        cnt, s = remove_zero(s)
        count_zero += cnt

        tmp = ''.join(to_binary(len(s)))
        count_binary += 1

        tmp = int(tmp)
        s = str(tmp)

    answer = [count_binary, count_zero]

    return answer

print(solution('110010101001'))
print(solution('01110'))
print(solution('1111111'))