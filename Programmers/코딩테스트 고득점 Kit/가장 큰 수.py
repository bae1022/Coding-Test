def solution(numbers):
    numbers_str = [str(num) for num in numbers]

    numbers_str.sort(key=lambda num: num*3, reverse=True)
    # lambda x:x*3 은 인자 각각의 문자열을 3번 반복한다는 의미
    # x * 3을 하는 이유는 num의 인수 값이 1000 이하이므로 3자리수로 맞춘 후에 비교한다는 의미이다.

    return str(int(''.join(numbers_str)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0,0]))