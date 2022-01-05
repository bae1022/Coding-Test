def solution(n):
    answer = 0

    def change(num):
        result = ''

        while num > 1:
            result += str(num % 2)
            num = num // 2
        result += str(num)

        return result[::-1]

    n_cnt1 = change(n).count('1')

    while True:
        n += 1

        tmp_cnt = change(n).count('1')

        if tmp_cnt == n_cnt1:
            break

    return n

print(solution(78)) # 83
print(solution(15)) # 23