def solution(s):
    answer = 0

    t = ''
    temp = ''
    for i in range(len(s)):
        if s[i].isalpha():
            temp += s[i]
            if temp == 'zero':
                t += '0'
                temp = ''

            if temp == 'one':
                t += '1'
                temp = ''

            if temp == 'two':
                t += '2'
                temp = ''

            if temp == 'three':
                t += '3'
                temp = ''

            if temp == 'four':
                t += '4'
                temp = ''

            if temp == 'five':
                t += '5'
                temp = ''

            if temp == 'six':
                t += '6'
                temp = ''

            if temp == 'seven':
                t += '7'
                temp = ''

            if temp == 'eight':
                t += '8'
                temp = ''

            if temp == 'nine':
                t += '9'
                temp = ''

        else:
            t += s[i]

    answer = int(t)
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))