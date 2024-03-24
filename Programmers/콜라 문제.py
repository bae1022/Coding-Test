def solution(a, b, n):

    #콜라를 받기 위해 마트에 주어야 하는 병 수: a
    #빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수: b
    #상빈이가 가지고 있는 빈 병의 개수: n
    answer = 0

    while (n >= a):
        t1 = n // a * b # t1: 빈 병 주고 받을 수 있는 콜라
        t2 = n % a

        n = t1 + t2
        answer = answer + t1

    return answer

print(solution(2, 1, 20)) # 19
print(solution(3, 1, 20)) # 9